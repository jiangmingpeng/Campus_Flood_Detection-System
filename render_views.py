# -*- coding: utf-8 -*-
"""
04_views 视图渲染脚本（在 FreeCAD GUI 的 Python 控制台里执行）

为什么不直接用 v.fitAll()：
    fitAll 会把整个场景（含 App::Annotation 标注、虚线示意路径等）一起套进视野，
    这块实验台是 800x500x~100 的“又宽又扁”的模型，fitAll 后正视/侧视会被缩得只剩
    画面中间一小条。

为什么也不手工摆 cam.position：
    coin 相机节点的 position 在**视图坐标系**里（vs 世界坐标），手算位置会整体平移画面；
    正交相机真正决定“视野大小”的只有 height（+ near/far 裁剪面）。
    实测正确姿势（本脚本采用，已在 FreeCAD 1.1.4 上逐张核对）：
        1) setCameraOrientation(rot)   —— 显式给基向量（视角按钮是异步的，别用 viewFront()）
        2) ViewFit                     —— 让 FreeCAD 自己把相机放到包围球中心、算好裁剪面
        3) cam.height = max(v_ext, u_ext/asp) * margin
                                       —— 再按可见实体的**顶点**投影跨度收窄视野，
                                          每张图正好填满画面并留 margin 白边
    注意 aspectRatio 会在 updateGui()/saveImage() 时被窗口比例覆盖，所以**不要**设它，
    也不要用它算 height；saveImage 会按请求的 w/h 重新排布，画面比例以 w/h 为准。

用法（FreeCAD GUI 控制台或 RPC execute_code）：
    src = open('//wsl.localhost/Ubuntu/home/jmp/text_to_cad/CAD/render_views.py',
               encoding='utf-8').read()
    exec(compile(src, 'render_views.py', 'exec'))
    render_views('//wsl.localhost/Ubuntu/home/jmp/text_to_cad/CAD/04_views')

输出（与 02_交付说明与验证.md 一致）：
    iso.png  top.png  front.png  right.png  iso_labeled.png
"""
import os
import time

import FreeCAD as App
import FreeCADGui as Gui

DOC_NAME = 'CampusFloodBench_V1'

# (文件名, 视角, 像素宽, 像素高, 边距系数, 是否显示标注)
VIEWS = (
    ('iso',         'iso',   1600, 1050, 1.07, False),
    ('top',         'top',   1600, 1050, 1.07, False),
    ('front',       'front', 1600,  360, 1.06, False),
    ('right',       'right', 1600,  360, 1.06, False),
    ('iso_labeled', 'iso',   1700, 1100, 1.18, True),
)

# 视角 = (观察方向 fwd, 相机 up)。注意 FreeCAD 的视角按钮是异步投递的，
# 走过 viewFront() 后立刻读相机节点会拿到**上一个**视角，所以这里显式给基向量。
# iso：相机位于 +X/-Y/+Z（右前上方）看向原点，fwd 就是 (-1, 1, -1)。
#      历史上写成 (1,-1,1) 会把相机放到板子**下面**，底板背面挡住模型 → 空图/局部图。
_ORIENT = {
    'iso':   (App.Vector(-1, 1, -1), App.Vector(0, 0, 1)),
    'top':   (App.Vector(0, 0, -1),  App.Vector(0, 1, 0)),
    'front': (App.Vector(0, 1, 0),   App.Vector(0, 0, 1)),
    'right': (App.Vector(-1, 0, 0),  App.Vector(0, 0, 1)),
}


# ---------------------------------------------------------------- 标注显隐
def _label_objects(doc):
    """收集标注，用来在“干净视图”里临时关掉"""
    out = []
    g = doc.getObject('_14_Labels')
    if g is not None:
        out.append(g)
    for o in doc.Objects:
        if o.TypeId == 'App::Annotation':
            out.append(o)
    return out


def _show_labels(doc, show):
    for o in _label_objects(doc):
        try:
            o.ViewObject.Visibility = bool(show)
        except Exception:
            pass


# ---------------------------------------------------------------- 包围盒
def _shapes_bbox(doc):
    """只统计可见的实体（忽略标注/直线等非 Shape 对象）"""
    bb = None
    for o in doc.Objects:
        try:
            if not o.ViewObject.Visibility:
                continue
        except Exception:
            continue
        if not hasattr(o, 'Shape') or o.Shape.isNull():
            continue
        b = o.Shape.BoundBox
        if b.XLength <= 0 and b.YLength <= 0 and b.ZLength <= 0:
            continue
        if bb is None:
            bb = App.BoundBox(b)
        else:
            bb.add(b)
    return bb


def _camera_rotation(direction, up):
    """由 (观察方向, up) 构造 coin 相机朝向：相机朝 -Z 看、+Y 为上"""
    fwd = App.Vector(direction).normalize()
    z_axis = -fwd
    up = App.Vector(up)
    up = (up - fwd * up.dot(fwd)).normalize()          # 正交化
    right = up.cross(z_axis).normalize()
    m = App.Matrix()
    m.A11, m.A21, m.A31 = right.x, right.y, right.z     # 第 1 列 = 相机 X
    m.A12, m.A22, m.A32 = up.x, up.y, up.z              # 第 2 列 = 相机 Y
    m.A13, m.A23, m.A33 = z_axis.x, z_axis.y, z_axis.z  # 第 3 列 = 相机 Z
    return App.Rotation(m), right, up, fwd


# 顶点采样上限：超过就退回用该对象的包围盒角点（对超密网格省时间）
_MAX_VERTS = 4000


def _projected_extent(doc, rot):
    """可见实体在相机 right/up 方向上的实际投影跨度 (u_ext, v_ext)

    用**顶点**而不是包围盒角点：iso 视角下包围盒 8 个角点会把对角线一起算进去，
    投影跨度虚大 30%~50%，画面就白白多出白边。顶点只有内部构件真实轮廓，
    画出来的墨迹边界才和预期一致（1548 个顶点，毫秒级）。
    """
    bb = _shapes_bbox(doc)
    if bb is None:
        return None
    c0 = bb.Center
    right = rot.multVec(App.Vector(1, 0, 0))
    up = rot.multVec(App.Vector(0, 1, 0))
    u_min = v_min = 1e30
    u_max = v_max = -1e30
    for o in doc.Objects:
        try:
            if not o.ViewObject.Visibility:
                continue
        except Exception:
            continue
        if not hasattr(o, 'Shape') or o.Shape.isNull():
            continue
        shape = o.Shape
        pts = []
        verts = shape.Vertexes
        if 0 < len(verts) <= _MAX_VERTS:
            pts = [v.Point for v in verts]
        else:
            b = shape.BoundBox
            if b.XLength <= 0 and b.YLength <= 0 and b.ZLength <= 0:
                continue
            pts = [App.Vector(x, y, z)
                   for x in (b.XMin, b.XMax)
                   for y in (b.YMin, b.YMax)
                   for z in (b.ZMin, b.ZMax)]
        for p in pts:
            d = p - c0
            u = d.dot(right)
            v = d.dot(up)
            if u < u_min:
                u_min = u
            if u > u_max:
                u_max = u
            if v < v_min:
                v_min = v
            if v > v_max:
                v_max = v
    if u_max < u_min:
        return None
    return u_max - u_min, v_max - v_min


def _frame(v, rot, aspect, margin):
    """ViewFit 之后只改 height，把视野收到可见实体的投影跨度上，返回 (u_ext, v_ext)

    不改 cam.position（因上面说过的视图坐标系问题），也不改 aspectRatio（会被覆盖）；
    正交相机下 height 是画面竖直方向的世界跨度，宽度 = height * 画面宽高比。
    """
    doc = App.getDocument(DOC_NAME)
    ext = _projected_extent(doc, rot)
    if ext is None:
        return None
    u_ext, v_ext = ext
    node = v.getCameraNode()
    node.height.setValue(max(v_ext, u_ext / float(aspect)) * float(margin))
    return ext


# ---------------------------------------------------------------- 主流程
def render_views(outdir, views=VIEWS):
    doc = App.getDocument(DOC_NAME)
    try:
        Gui.activateWorkbench('PartWorkbench')
    except Exception:
        pass
    v = Gui.activeDocument().activeView()
    try:
        v.setCameraType('Orthographic')
    except Exception:
        pass

    made = []
    for (name, orient, w, h, margin, labeled) in views:
        _show_labels(doc, labeled)
        rot, _r, _u, _f = _camera_rotation(*_ORIENT[orient])
        v.setCameraOrientation(rot)
        Gui.updateGui()
        time.sleep(0.10)
        Gui.SendMsgToActiveView('ViewFit')       # 先把相机摆正、裁剪面算好
        Gui.updateGui()
        time.sleep(0.20)
        ext = _frame(v, rot, w / float(h), margin)   # 再按真实投影跨度定 height
        Gui.updateGui()
        time.sleep(0.20)
        path = os.path.join(outdir, name + '.png')
        v.saveImage(path, w, h, 'White')
        Gui.updateGui()
        made.append((name, path, os.path.getsize(path), ext))
        App.Console.PrintMessage(u'[views] %s -> %s (%d bytes, ext=%s)\n'
                                 % (name, path, os.path.getsize(path), ext))

    _show_labels(doc, True)          # 恢复标注，别把文档搞乱
    rot, _r, _u, _f = _camera_rotation(*_ORIENT['iso'])
    v.setCameraOrientation(rot)
    Gui.updateGui()
    Gui.SendMsgToActiveView('ViewFit')
    return made
