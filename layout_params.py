# -*- coding: utf-8 -*-
"""
layout_params.py
校园大面积积水应急排水实验台 V1.0 —— 布局参数表（唯一数据源，单位 mm）

坐标系：X 向右 / Y 向后 / Z 向上；原点 = 底板左下角外侧底面，Z=0 为底板底面。
约定：每个部件用包围盒 (x, y, z, lx, ly, lz) 描述，x/y/z 取最小角点。
      地面层对象默认坐到 z = BASE_T（底板上表面）。
"""

# ---------------------------------------------------------------------------
# 0. 全局参数
# ---------------------------------------------------------------------------
BASE_L, BASE_W, BASE_T = 800.0, 500.0, 8.0

WALL = 3.0          # 水槽通用壁厚
FLOOR_T = 3.0       # 水槽通用底厚
HOSE_R = 4.0        # 软管半径（外径 8）
ROAD_T = 3.0        # 道路面层厚
MARK_T = 1.0        # 地面标线厚

# A 区：宿舍门口积水浅坑（V1.2 布局重排：宿舍居左 / 自行车道紧跟其右 / 浅坑 X 向加宽包住两者）
# 底板仅 8 mm，无法直接下挖 → 靠"门前地坪加厚 13 mm"造出真实下沉：
#   地坪 13（8→21）、槽底 3（8→11）→ 槽内底面比地坪面低 10 mm（A_SINK）
# 水槽总高 35（8→43）；南（朝 C）/东（朝 B）只做 15 mm 路缘台阶（顶面 23）+ 坑内缓坡。
# 平面顺序（自西向东）：宿舍楼（基座当西/北墙）→ 自行车停放台（坑内孤岛）→ 东侧开敞水面 75 mm。
# 浅坑 X 向外廓由 130 加宽到 204（y、35 高、10 下沉、缓坡全部不变），把宿舍基座和整条自行车道都包进积水区。
A_TANK_X, A_TANK_Y, A_TANK_Z = 204.0, 145.0, 35.0
A_TANK_POS = (84.0, 320.0, BASE_T)
A_SINK = 10.0
A_APRON_T = A_SINK + FLOOR_T                  # 13
A_APRON_BOX = (84.0, 320.0, 288.0, 480.0)     # 门前地坪外框 x0, y0, x1, y1
A_CURB_H = 15.0                               # 朝 C/B 路缘台阶高（自底板顶面算）
A_RAMP_RUN = 22.0                             # 缓坡水平投影
A_WATER_LEVEL = 11.0                          # 相对槽内底面 → 水面 22（比路缘顶低 1）
A_DORM = (84.0, 365.0, 60.0, 100.0, 95.0)     # 宿舍楼居最左，基座充当西/北两面墙
A_BIKE = (154.0, 350.0, 56.0, 110.0)          # 自行车停放台（坑内孤岛）x0, y0, lx, ly
A_BIKE_BAR_L, A_BIKE_BAR_W, A_BIKE_BAR_H = 44.0, 8.0, 5.0   # 自行车占位块（3 条）
A_FLOOR_Z = BASE_T + FLOOR_T                  # 11
A_APRON_Z = BASE_T + A_APRON_T                # 21
A_CURB_Z = BASE_T + A_CURB_H                  # 23
A_RIM_Z = BASE_T + A_TANK_Z                   # 43
A_WATER_Z = A_FLOOR_Z + A_WATER_LEVEL         # 22

# B 区（按 drawio 几何：北侧大面积浅水盘 + 南侧"面积大、相对较浅"观察区 + 南缘石块路）
B_X, B_Y, B_PLATE_T = 250.0, 180.0, 20.0
B_POS = (338.0, 300.0, BASE_T)
B_BASIN = (358.0, 370.0, 210.0, 86.0, 6.0)      # S3 主浅水面，下沉 6 → 槽底 z=22
B_S2AREA = (360.0, 328.0, 212.0, 36.0, 4.0)     # S2 观察区（大面积、相对较浅），下沉 4 → 槽底 z=24
B_LOW = (470.0, 332.0, 46.0, 26.0, 10.0)        # 局部低洼（积水较深），下沉 10 → 槽底 z=18
B_MOUND = (360.0, 372.0, 54.0, 84.0)            # 草坪边缘局部高地（z 22→28，露出水面）
B_STONE = (344.0, 306.0, 238.0, 16.0)           # 石块路，顶面 z=32（高于草坪面板 28）
B_WATER_S3_Z = 26.0                             # 主浅水面（槽底 22 → 水深 4）
B_WATER_S2_Z = 26.0                             # S2 水面同高（低洼槽底 18 → 水深 8）

# C 区
ROAD_Y0, ROAD_Y1 = 182.0, 288.0
C_TRAY = (78.0, 190.0, 220.0, 62.0, 10.0)       # x, y, lx, ly, 高（坐于道路面 11 上，落在 A 区下方）
C_TRAY_WATER_LEVEL = 4.0

# C 区 · P1 挡水台阶（V1.1：由"下沉 3 mm 凹位"改为 15 mm 浅台，兼泵停放位）
# 可用进深受两侧既有件夹住：浅水盘占 y 190~252、A 区地坪自 y=320 起 → 最大 68
# （路面内 36 + 向北越过路缘拓出 32）；泵长边沿路停放：110 沿 X / 60 沿 Y，两侧各留 4。
# 台阶顶面 23 = A 区路缘台阶顶面 → 水从 A 区漫过路缘后先铺满台阶，再溢流进浅水盘。
P1_BAY_X, P1_BAY_Y = 96.0, 252.0
P1_BAY_LX, P1_BAY_LY = 136.0, 68.0
P1_STEP_H = 15.0
P1_STEP_Z = BASE_T + P1_STEP_H                # 23

# D 区
D_POS = (596.0, 375.0, BASE_T)
D_L, D_W, D_H = 194.0, 115.0, 22.0
SLOPE_N = 6

# E 泵
PUMP_POS = (95.0, 30.0, BASE_T)
PUMP_L, PUMP_W, PUMP_BASE_H = 110.0, 60.0, 6.0

# F 回收水箱
TANK_POS = (300.0, 25.0, BASE_T)
TANK_L, TANK_W, TANK_H = 100.0, 70.0, 45.0
TANK_WATER_LEVEL = 12.0

# G 电子区
ELEC_POS = (465.0, 20.0, BASE_T)
ELEC_L, ELEC_W, ELEC_PAD_H = 320.0, 125.0, 6.0

# ---------------------------------------------------------------------------
# 走线（V1.3）：贴地实体线槽 + 示意线缆
# ---------------------------------------------------------------------------
# 可用空档（实测）：底部设备带（泵 / 回收水箱 / 电子区）上缘 y=145，主路下缘 y=182
# → 中间有一条 37 mm 通贯空档。主线槽落在 y152~172（宽 20、高 6，坐底板顶面），
#   离电子区 7 mm、离主路 10 mm，全程不压泵(y≤90)、水箱(y≤95)、干燥垫(y≤145) 与路面(y≥182)，
#   也不挡 MOVE_2 人工搬运线（y=150，留 2 mm）。
# 竖向干线槽沿 A/B 连接路西缘（x300~320）北上到 y486，再分三路支线槽接 S1/S2/S3。
CABLE_DUCT_Y = 152.0          # 主线槽南边 Y
CABLE_DUCT_W = 20.0           # 主线槽宽
CABLE_DUCT_H = 6.0            # 线槽高（坐底板顶面 → z 8~14）
CABLE_DUCT_X0, CABLE_DUCT_X1 = 10.0, 785.0
CABLE_DUCT_T = 1.5            # 槽壁 / 槽底厚
CABLE_DUCT_TRUNK_X = 300.0    # 竖向干线槽西边 X（= 连接路西缘）
CABLE_DUCT_PAD_Y = 135.0      # 电子区内走线槽南边 Y（贴三个盒体北壁）
CABLE_PAD_GAP = (626.0, 74.0) # 挡水圈北带出线缺口 (x0, 宽)
CABLE_R = 2.0                 # 线缆半径（外径 4）
CABLE_Z_MAIN = BASE_T + 3.75  # 主线槽内敷设高度（内腔 z 9.5~14）
CABLE_Z_TRUNK = BASE_T + ROAD_T + 3.75

GROUPS = ['01_Base', '02_Zone_A_Dormitory', '03_Zone_B_Woodland', '04_Zone_C_Roads',
          '05_Zone_D_Highland', '06_Pump_Module', '07_Recovery_Tank', '08_Electronics',
          '09_Sensors', '10_Hoses', '11_Movement_Paths', '12_Communication_Lines',
          '13_Water_Surface_Reference', '14_Labels', '15_Cabling']


def P(g, n, x, y, z, lx, ly, lz, k='box', **kw):
    d = dict(g=g, n=n, x=x, y=y, z=z, lx=lx, ly=ly, lz=lz, k=k)
    d.update(kw)
    return d


def cx(name, x0, length, r, cy_, cz_, g, col):
    """沿 X 轴圆柱（包围盒 + 圆柱描述）"""
    return dict(g=g, n=name, x=x0, y=cy_ - r, z=cz_ - r, lx=length, ly=2 * r, lz=2 * r,
                cyl=('x', x0, length, r, cy_, cz_), col=col, k='cyl')


def cy_(name, xc, y0, length, r, cz_, g, col):
    """沿 Y 轴圆柱"""
    return dict(g=g, n=name, x=xc - r, y=y0, z=cz_ - r, lx=2 * r, ly=length, lz=2 * r,
                cyl=('y', xc, y0, length, r, cz_), col=col, k='cyl')


def a_apron_pieces():
    """门前地坪分件（西侧自行车带 / 北侧散水 / 东侧贴 A/B 连接路），中间留槽体洞口。"""
    x0, y0, x1, y1 = A_APRON_BOX
    tx0, ty0 = A_TANK_POS[0], A_TANK_POS[1]
    tx1, ty1 = tx0 + A_TANK_X, ty0 + A_TANK_Y
    out = []
    for (bx, by, blx, bly) in ((x0, y0, tx0 - x0, y1 - y0),
                               (tx0, ty1, tx1 - tx0, y1 - ty1),
                               (tx1, y0, x1 - tx1, y1 - y0)):
        if blx > 0 and bly > 0:
            out.append((bx, by, BASE_T, blx, bly, A_APRON_T))
    return out


def a_tank_pieces():
    """A 区浅坑槽体分件：3 mm 底板（挖去宿舍占位）+ 南/东路缘 15 + 西/北全高墙 35。
    缓坡另作斜面棱柱（prism 字段），检查时按同一包围盒登记。"""
    x0, y0 = A_TANK_POS[0], A_TANK_POS[1]
    x1, y1 = x0 + A_TANK_X, y0 + A_TANK_Y
    zf, zc, zr = A_FLOOR_Z, A_CURB_Z, A_RIM_Z
    dx0, dy0, dlx, dly, _ = A_DORM
    return [
        (x0, y0, BASE_T, A_TANK_X, dy0 - y0, FLOOR_T),                      # 槽底板（南段）
        (dx0 + dlx, dy0, BASE_T, x1 - (dx0 + dlx), y1 - dy0, FLOOR_T),      # 槽底板（东+北）
        (x0, y0, zf, A_TANK_X, WALL, zc - zf),                              # 南路缘（朝 C）
        (x1 - WALL, y0, zf, WALL, A_TANK_Y, zc - zf),                       # 东路缘（朝 B）
        (x0, y0, zf, WALL, dy0 - y0, zr - zf),                              # 西墙（余段）
        (dx0 + dlx, y1 - WALL, zf, x1 - (dx0 + dlx), WALL, zr - zf),        # 北墙（余段）
        (x0 + WALL, y0 + WALL, zf, (x1 - WALL - A_RAMP_RUN) - (x0 + WALL),
         A_RAMP_RUN, zc - zf),                                              # 缓坡（朝 C）
        (x1 - WALL - A_RAMP_RUN, y0 + WALL + A_RAMP_RUN, zf, A_RAMP_RUN,
         y1 - WALL - (y0 + WALL + A_RAMP_RUN), zc - zf),                    # 缓坡（朝 B）
    ]


def parts_A():
    o, g = [], '02_Zone_A_Dormitory'
    dx0, dy0, dlx, dly, dlz = A_DORM
    o.append(P(g, 'Dormitory_Model', dx0, dy0, BASE_T, dlx, dly, dlz, col='bldg'))
    ap = a_apron_pieces()
    o.append(P(g, 'A_Zone_Apron', min(a[0] for a in ap), min(a[1] for a in ap), BASE_T,
               max(a[0] + a[3] for a in ap) - min(a[0] for a in ap),
               max(a[1] + a[4] for a in ap) - min(a[1] for a in ap), A_APRON_T,
               boxes=ap, k='apron', col='grey'))
    # 自行车停放台：坑内孤岛，台面 21 = 地坪面，比水面 22 低 1 → 水漫过停车道板面
    bx0, by0, blx, bly = A_BIKE
    o.append(P(g, 'Bicycle_Parking', bx0, by0, A_FLOOR_Z, blx, bly,
               A_APRON_Z - A_FLOOR_Z, col='bike'))
    gap = (bly - 3.0 * A_BIKE_BAR_W) / 4.0
    for i in range(3):
        o.append(P(g, 'Bike_Placeholder_0%d' % (i + 1),
                   bx0 + (blx - A_BIKE_BAR_L) / 2.0,
                   by0 + gap + i * (A_BIKE_BAR_W + gap), A_APRON_Z,
                   A_BIKE_BAR_L, A_BIKE_BAR_W, A_BIKE_BAR_H, col='dark'))
    tk = a_tank_pieces()
    o.append(P(g, 'A_Deep_Water_Tank', A_TANK_POS[0], A_TANK_POS[1], BASE_T,
               A_TANK_X, A_TANK_Y, A_TANK_Z, boxes=tk, k='tankasm', col='atank'))
    # 注水口 / 可调排水口：都落在宿舍以南那段西墙（x 84~87、y 320~365）上
    o.append(cx('A_Tank_Inlet_Port', 70, 18, 5, 334, 35, g, 'pipe'))
    o.append(cx('A_Tank_Drain_Port', 72, 18, 5, 352, 15, g, 'pipe'))
    o.append(P(g, 'A_Tank_Drain_Adjuster', 87, 345, A_FLOOR_Z, 3, 14, 22, col='metal'))
    o.append(cy_('A_Tank_Overflow_Port', 240, 458, 16, 4, 32, g, 'pipe'))
    o.append(cy_('A_Tank_Suction_Port', 240, 306, 22, 5, 20, g, 'pipe'))
    return o


def parts_B():
    o, g = [], '03_Zone_B_Woodland'
    o.append(P(g, 'B_Woodland_Base', B_POS[0], B_POS[1], B_POS[2], B_X, B_Y, B_PLATE_T,
               k='terrain', cut=[B_BASIN, B_S2AREA, B_LOW], col='grass'))
    o.append(P(g, 'B_Raised_Mound', B_MOUND[0], B_MOUND[1], 22, B_MOUND[2], B_MOUND[3], 6,
               col='grass2'))
    o.append(P(g, 'B_Stone_Path', B_STONE[0], B_STONE[1], 28, B_STONE[2], B_STONE[3], 4,
               col='stone'))
    o.append(cx('B_Inlet_Port', 588, 18, 5, 340, 13, g, 'pipe'))
    o.append(cy_('B_Drain_Port', 540, 290, 26, 5, 13, g, 'pipe'))
    o.append(cx('B_Suction_Port', 326, 20, 6, 336, 25, g, 'pipe'))
    # 注：原"四棵树"（B_Tree_01~04）已按要求删除，B 区只保留地形板 / 局部高地 / 石块路。
    return o


def parts_C():
    o, g = [], '04_Zone_C_Roads'
    road = P(g, 'C_Main_Road', 15, ROAD_Y0, BASE_T, 585, ROAD_Y1 - ROAD_Y0, ROAD_T, col='road')
    road['notch'] = (P1_BAY_X, P1_BAY_Y, P1_BAY_LX)      # P1 段路面层挖掉（给 15 mm 挡水台阶让位）
    o.append(road)
    o.append(P(g, 'C_Connector_Road', 288, ROAD_Y1, BASE_T, 44, 200, ROAD_T, col='road'))
    o.append(P(g, 'C_Ring_Road', 600, 180, BASE_T, 190, 108, ROAD_T, k='ring', band=18, col='road'))
    o.append(P(g, 'C_Road_Water_Tray', C_TRAY[0], C_TRAY[1], BASE_T + ROAD_T,
               C_TRAY[2], C_TRAY[3], C_TRAY[4], k='tank', wall=WALL, floor_t=FLOOR_T, col='tray'))
    o.append(P(g, 'C_Tray_Sight_Glass', 228, 187, 12, 34, 3, 8, k='glass', col='glass'))
    o.append(cy_('C_Tray_Inlet_Port', 250, 252, 18, 5, 19, g, 'pipe'))
    o.append(cy_('C_Tray_Drain_Port', 270, 178, 18, 4, 15, g, 'pipe'))
    # P1 挡水台阶：15 mm 浅台（顶面 23 = A 区路缘台阶顶面），台面上红边框线 + 泵停放占位
    o.append(P(g, 'P1_Bay_Step', P1_BAY_X, P1_BAY_Y, BASE_T,
               P1_BAY_LX, P1_BAY_LY, P1_STEP_H, col='road'))
    o.append(P(g, 'P1_Bay_Edge_Marking', P1_BAY_X, P1_BAY_Y, P1_STEP_Z,
               P1_BAY_LX, P1_BAY_LY, MARK_T, k='ring', band=2, col='red'))
    o.append(P(g, 'P1_Candidate_Stop',
               P1_BAY_X + (P1_BAY_LX - PUMP_L) / 2.0, P1_BAY_Y + (P1_BAY_LY - PUMP_W) / 2.0,
               P1_STEP_Z, PUMP_L, PUMP_W, MARK_T, col='red'))
    o.append(P(g, 'P2_Candidate_Stop', 366, 258, BASE_T + ROAD_T, 105, 26, MARK_T, col='red'))
    o.append(P(g, 'P3_Candidate_Stop', 296, 300, BASE_T + ROAD_T, 34, 30, MARK_T, col='red'))
    o.append(P(g, 'C_Dry_Parking', 450, 190, BASE_T + ROAD_T, 145, 62, 2, col='green'))
    return o


def parts_D():
    o, g = [], '05_Zone_D_Highland'
    o.append(P(g, 'D_Highland', D_POS[0], D_POS[1], D_POS[2], D_L, D_W, D_H, col='high'))
    o.append(P(g, 'D_Highland_Top_Step', 616, 392, D_POS[2] + D_H, 154, 81, 6, col='high2'))
    y0, y1 = ROAD_Y1, D_POS[1]
    dy = (y1 - y0) / SLOPE_N
    z_top, z_end = D_POS[2] + D_H, BASE_T + ROAD_T
    for i in range(SLOPE_N):
        yi = y1 - (i + 1) * dy
        zi = z_top - (i + 1) * (z_top - z_end) / SLOPE_N
        o.append(P(g, 'B_Right_Slope_Step_%d' % (i + 1), 610, yi, BASE_T, 170, dy,
                   zi - BASE_T, k='step', col='road'))
    return o


def parts_E():
    o, g = [], '06_Pump_Module'
    o.append(P(g, 'Pump_Module_Base', PUMP_POS[0], PUMP_POS[1], PUMP_POS[2],
               PUMP_L, PUMP_W, PUMP_BASE_H, col='pump'))
    o.append(cx('Pump_Body', 112, 44, 17, 60, 31, g, 'pump2'))
    o.append(cx('Pump_Motor', 156, 34, 14, 60, 31, g, 'metal'))
    o.append(cx('Pump_Suction_Port', 92, 20, 5, 60, 25, g, 'pipe'))
    o.append(cy_('Pump_Suction_Port_Alt', 150, 70, 34, 5, 25, g, 'pipe'))
    o.append(cx('Pump_Discharge_Port', 190, 20, 5, 60, 25, g, 'pipe'))
    o.append(P(g, 'Flow_Sensor_Block', 95, 52, 18, 16, 16, 14, col='sensor'))
    o.append(P(g, 'Current_Sensor_Block', 191, 75, 14, 14, 14, 12, col='sensor'))
    o.append(P(g, 'Pump_Controller_Connector', 98, 31, 14, 20, 11, 10, col='sensor'))
    return o


def parts_F():
    g = '07_Recovery_Tank'
    return [
        P(g, 'Recovery_Tank', TANK_POS[0], TANK_POS[1], TANK_POS[2],
          TANK_L, TANK_W, TANK_H, k='tank', wall=WALL, floor_t=FLOOR_T, col='recov'),
        cx('Recovery_Tank_Inlet_Port', 292, 14, 5, 48, 25, g, 'pipe'),
        cy_('Recovery_Tank_Drain_Port', 340, 17, 16, 5, 13, g, 'pipe'),
        cy_('Recovery_Tank_Drain_Handle', 340, 10, 8, 5, 13, g, 'metal'),
        P(g, 'Recovery_Tank_Level_Window', 352, 22, 14, 22, 3, 30, k='glass', col='glass'),
        cx('Recovery_Tank_Overflow_Port', 397, 14, 5, 70, 42, g, 'pipe'),
    ]


def parts_G():
    o, g = [], '08_Electronics'
    ex, ey, ez = ELEC_POS
    o.append(P(g, 'Electronics_Zone_Pad', ex, ey, ez, ELEC_L, ELEC_W, ELEC_PAD_H, col='elec'))
    o.append(P(g, 'Electronics_Zone_Curb', ex, ey, ez + ELEC_PAD_H, ELEC_L, ELEC_W, 8,
               k='ring', band=5, gap=CABLE_PAD_GAP, col='elec2'))
    o.append(P(g, 'Linux_Main_Controller_Box', 475, 28, 14, 150, 100, 34,
               k='tank', wall=WALL, floor_t=FLOOR_T, col='elec'))
    o.append(P(g, 'Linux_Mainboard_Placeholder', 483, 36, 17, 130, 80, 2, col='pcb'))
    o.append(P(g, 'MCU_Sensor_Node_Box', 640, 80, 14, 80, 55, 22,
               k='tank', wall=WALL, floor_t=FLOOR_T, col='elec'))
    o.append(P(g, 'MCU_Sensor_Board', 651, 90, 17, 62, 40, 2, col='pcb'))
    o.append(P(g, 'MCU_Pump_Node_Box', 640, 26, 14, 75, 50, 22,
               k='tank', wall=WALL, floor_t=FLOOR_T, col='elec'))
    o.append(P(g, 'MCU_Pump_Board', 650, 33, 17, 58, 36, 2, col='pcb'))
    o.append(P(g, 'Power_Interface_Block', 732, 96, 14, 44, 34, 12, col='pcb'))
    return o


# ---------------------------------------------------------------------------
# 走线（15_Cabling）：实体线槽（U 形，两端开口）+ 示意线缆
# ---------------------------------------------------------------------------
def duct(x, y, z, lx, ly, lz, t=CABLE_DUCT_T):
    """U 形线槽分件：底板 + 南/北两壁（顶部与两端开口），返回 3 个 [x,y,z,lx,ly,lz]。"""
    return [(x, y, z, lx, ly, t),
            (x, y, z + t, lx, t, lz - t),
            (x, y + ly - t, z + t, lx, t, lz - t)]


def parts_cabling():
    """线槽（进空间检查）+ 线缆（敷设层，与线槽/其他线缆不互判干涉）。"""
    g = '15_Cabling'
    o = []
    dy, dw, dh = CABLE_DUCT_Y, CABLE_DUCT_W, CABLE_DUCT_H
    dz = BASE_T
    # 1) 主线槽：底板通贯横槽（设备带与主路之间的 37 mm 空档内）
    o.append(P(g, 'Cable_Duct_Main', CABLE_DUCT_X0, dy, dz,
               CABLE_DUCT_X1 - CABLE_DUCT_X0, dw, dh, k='duct', col='duct',
               boxes=duct(CABLE_DUCT_X0, dy, dz, CABLE_DUCT_X1 - CABLE_DUCT_X0, dw, dh)))
    # 2) 竖向干线槽：主线槽 → 连接路（底板段 z8~14，路面段 z11~17，各自坐在所在面上）
    tx = CABLE_DUCT_TRUNK_X
    o.append(P(g, 'Cable_Duct_Trunk_N', tx, dy + dw, dz,
               dw, 182 - (dy + dw), dh, k='duct', col='duct',
               boxes=duct(tx, dy + dw, dz, dw, 182 - (dy + dw), dh)))
    o.append(P(g, 'Cable_Duct_Trunk_S', tx, 182, dz + ROAD_T,
               dw, 486 - 182, dh, k='duct', col='duct',
               boxes=duct(tx, 182, dz + ROAD_T, dw, 486 - 182, dh)))
    # 3) 电子区内走线槽：贴三个盒体北壁，收集盒内线缆（窄槽 10 宽，在干燥垫面 z14~20）
    o.append(P(g, 'Cable_Duct_Pad', 472, CABLE_DUCT_PAD_Y, dz + ELEC_PAD_H,
               306, 10, dh, k='duct', col='duct',
               boxes=duct(472, CABLE_DUCT_PAD_Y, dz + ELEC_PAD_H, 306, 10, dh)))
    # 4) 出线口：挡水圈缺口下方、连接垫边与主线槽的短套（实心，7 mm 长）
    o.append(P(g, 'Cable_Duct_Outlet', 660, 145, dz, 36, 7, dh, k='duct', solid=True, col='duct'))
    # 5) 三路支线槽：S1 走门前散水面 / S2、S3 走 B 区地形板面
    o.append(P(g, 'Cable_Duct_Branch_S1', 240, 465, dz + A_APRON_T,
               60, 12, dh, k='duct', col='duct',
               boxes=duct(240, 465, dz + A_APRON_T, 60, 12, dh)))
    o.append(P(g, 'Cable_Duct_Branch_S2', 338, 342, dz + B_PLATE_T,
               40, 12, dh, k='duct', col='duct',
               boxes=duct(338, 342, dz + B_PLATE_T, 40, 12, dh)))
    o.append(P(g, 'Cable_Duct_Branch_S3', 338, 420, dz + B_PLATE_T,
               198, 12, dh, k='duct', col='duct',
               boxes=duct(338, 420, dz + B_PLATE_T, 198, 12, dh)))
    # ---- 线缆（R2）----
    cables = [
        # 主控 ↔ 两个 MCU：横穿 15 mm 间隙，贴干燥垫面（z 中心 16）
        ('Cable_Linux_MCU_Sensor', [(622, 104, 16), (643, 104, 16)]),
        ('Cable_Linux_MCU_Pump', [(622, 60, 16), (643, 60, 16)]),
        # MCU_感知 → S1：盒北壁 → 垫内线槽 → 出线口 → 主线槽 → 竖槽 → 散水面 → S1 底座
        ('Cable_MCU_Sensor_S1', [(680, 133, 17.75), (680, 147.5, 17.75), (680, 147.5, CABLE_Z_MAIN),
                                 (680, 155, CABLE_Z_MAIN), (305, 155, CABLE_Z_MAIN),
                                 (305, 170, CABLE_Z_MAIN), (305, 179, CABLE_Z_TRUNK),
                                 (305, 470, CABLE_Z_TRUNK), (297, 470, CABLE_Z_TRUNK),
                                 (297, 470, 24.75), (252, 470, 24.75), (252, 470, 45)]),
        # MCU_感知 → S2：同一干线，到 y347 东折，爬 B 板面进 S2 底座
        ('Cable_MCU_Sensor_S2', [(668, 133, 17.75), (668, 147.5, 17.75), (668, 147.5, CABLE_Z_MAIN),
                                 (668, 160, CABLE_Z_MAIN), (310, 160, CABLE_Z_MAIN),
                                 (310, 170, CABLE_Z_MAIN), (310, 179, CABLE_Z_TRUNK),
                                 (310, 347, CABLE_Z_TRUNK), (330, 347, CABLE_Z_TRUNK),
                                 (330, 347, 31.75), (378, 347, 31.75), (378, 347, 26)]),
        # MCU_感知 → S3：同一干线，到 y428 东折
        ('Cable_MCU_Sensor_S3', [(656, 133, 17.75), (656, 147.5, 17.75), (656, 147.5, CABLE_Z_MAIN),
                                 (656, 165, CABLE_Z_MAIN), (315, 165, CABLE_Z_MAIN),
                                 (315, 170, CABLE_Z_MAIN), (315, 179, CABLE_Z_TRUNK),
                                 (315, 428, CABLE_Z_TRUNK), (330, 428, CABLE_Z_TRUNK),
                                 (330, 428, 31.75), (536, 428, 31.75), (536, 432, 26)]),
        # MCU_泵控 → 泵控制器接口：绕泵体西侧，从接口前上方进入（避开水箱与泵体）
        ('Cable_MCU_Pump_Pump', [(642, 51, 17.75), (632, 51, 17.75), (632, 147.5, 17.75),
                                 (632, 147.5, CABLE_Z_MAIN), (632, 168, CABLE_Z_MAIN),
                                 (88, 168, CABLE_Z_MAIN), (88, 20, CABLE_Z_MAIN),
                                 (108, 20, 17), (108, 36, 17), (108, 36, 19)]),
    ]
    for n, pts in cables:
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        zs = [p[2] for p in pts]
        o.append(dict(g=g, n=n, x=min(xs) - CABLE_R, y=min(ys) - CABLE_R, z=min(zs) - CABLE_R,
                      lx=max(xs) - min(xs) + 2 * CABLE_R, ly=max(ys) - min(ys) + 2 * CABLE_R,
                      lz=max(zs) - min(zs) + 2 * CABLE_R,
                      k='cable', pts=pts, r=CABLE_R, col='cable'))
    return o


# ---------------------------------------------------------------------------
# 传感器（每个传感器 = 1 个可选/可隐藏对象，由底座+立柱+悬臂+探头组成）
# ---------------------------------------------------------------------------
def parts_sensors():
    """传感器 = 底座 + 立柱 + 悬臂 + 探头；boxes 为该对象的分件包围盒（宏中按此建实体）。"""
    g = '09_Sensors'
    o = []
    o.append(dict(g=g, n='Sensor_S1', x=240, y=436, z=16, lx=24, ly=43, lz=A_RIM_Z + 32 - 16,
                  boxes=[(240, 455, A_RIM_Z, 24, 24, 4),
                         (247, 458, A_RIM_Z + 4, 8, 8, 25),
                         (247, 436, A_RIM_Z + 29, 8, 28, 3),
                         (248, 442, 16, 6, 6, A_RIM_Z + 29 - 16)],
                  col='sensor'))
    o.append(dict(g=g, n='Sensor_S2', x=378, y=334, z=24, lx=50, ly=24, lz=19,
                  boxes=[(378, 334, 24, 24, 24, 4), (386, 342, 28, 8, 8, 16),
                         (402, 342, 40, 26, 8, 3), (422, 343, 25, 6, 6, 15)],
                  col='sensor'))
    o.append(dict(g=g, n='Sensor_S3', x=512, y=430, z=22, lx=48, ly=24, lz=20,
                  boxes=[(536, 430, 22, 24, 24, 4), (544, 438, 26, 8, 8, 16),
                         (512, 438, 38, 40, 8, 3), (512, 439, 23, 6, 6, 15)],
                  col='sensor'))
    return o


# ---------------------------------------------------------------------------
# 软管：折线 + 圆角肘部占位（半径 HOSE_R）
# ---------------------------------------------------------------------------
HOSE_1 = [(92, 60, 30), (72, 60, 30), (72, 296, 30), (240, 296, 30), (240, 306, 30),
          (240, 306, 20)]
HOSE_2 = [(150, 104, 25), (150, 120, 25), (292, 120, 25), (292, 336, 25), (330, 336, 25)]
HOSE_DR = [(210, 60, 25), (232, 60, 25), (232, 48, 25), (292, 48, 25)]


def _poly_bbox(pts, r):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    zs = [p[2] for p in pts]
    return dict(x=min(xs) - r, y=min(ys) - r, z=min(zs) - r,
                lx=max(xs) - min(xs) + 2 * r, ly=max(ys) - min(ys) + 2 * r,
                lz=max(zs) - min(zs) + 2 * r)


def parts_hoses():
    o, g = [], '10_Hoses'
    for n, pts in (('Hose_Suction_1', HOSE_1), ('Hose_Suction_2', HOSE_2), ('Hose_Drain', HOSE_DR)):
        d = _poly_bbox(pts, HOSE_R)
        d.update(g=g, n=n, k='hose', pts=pts, r=HOSE_R,
                 col={'Hose_Suction_1': 'hose1', 'Hose_Suction_2': 'hose2', 'Hose_Drain': 'hose3'}[n])
        o.append(d)
    return o


# ---------------------------------------------------------------------------
# 人工移动候选路线（黄色虚线，台面上方 9.5mm 的示意线）
# ---------------------------------------------------------------------------
MOVE_1 = [(60, 70, 9.5), (60, 270, 9.5), (212, 270, 9.5)]
MOVE_2 = [(150, 95, 9.5), (150, 150, 9.5), (418, 150, 9.5), (418, 270, 9.5)]
MOVE_3 = [(150, 98, 9.5), (150, 118, 9.5), (316, 118, 9.5), (316, 300, 9.5)]

# 数据通信（紫色虚线，架空逻辑总线 z=84，不与任何实体相交）
COMM_Z = 84.0
COMM_TRUNK = [(312, 455, COMM_Z), (312, 152, COMM_Z), (660, 152, COMM_Z),
              (660, 110, COMM_Z), (660, 110, 40)]
COMM_S1 = [(248, 450, A_RIM_Z + 32), (312, 450, COMM_Z)]
COMM_S2 = [(424, 346, 43), (424, 346, COMM_Z), (424, 346, COMM_Z), (312, 346, COMM_Z)]
COMM_S3 = [(552, 438, 41), (552, 438, COMM_Z), (552, 438, COMM_Z), (312, 438, COMM_Z)]
COMM_L1 = [(680, 84, 36), (680, 72, 36), (680, 72, 52), (618, 72, 52), (618, 72, 48)]
COMM_L2 = [(612, 60, 48), (612, 60, 58), (664, 60, 58), (664, 60, 36)]


def parts_paths():
    o = []
    for n, pts in (('Move_Path_01', MOVE_1), ('Move_Path_02', MOVE_2), ('Move_Path_03', MOVE_3)):
        o.append(dict(g='11_Movement_Paths', n=n, k='wire', pts=pts, style='dashed',
                      col='move', x=min(p[0] for p in pts), y=min(p[1] for p in pts),
                      z=min(p[2] for p in pts), lx=0, ly=0, lz=0))
    for n, pts in (('Comm_Trunk', COMM_TRUNK), ('Comm_S1_Link', COMM_S1),
                   ('Comm_S2_Link', COMM_S2), ('Comm_S3_Link', COMM_S3),
                   ('Comm_MCU_Sensor_To_Linux', COMM_L1), ('Comm_Linux_To_MCU_Pump', COMM_L2)):
        o.append(dict(g='12_Communication_Lines', n=n, k='wire', pts=pts, style='dashed',
                      col='comm', x=min(p[0] for p in pts), y=min(p[1] for p in pts),
                      z=min(p[2] for p in pts), lx=0, ly=0, lz=0))
    return o


def a_water_pieces():
    """A 区水面分件：扣壁厚后的槽内净空，并让开宿舍基座（L 形）。"""
    x0, y0 = A_TANK_POS[0] + WALL, A_TANK_POS[1] + WALL
    x1 = A_TANK_POS[0] + A_TANK_X - WALL
    y1 = A_TANK_POS[1] + A_TANK_Y - WALL
    dx0, dy0, dlx, _, _ = A_DORM
    return [(x0, y0, A_WATER_Z, x1 - x0, dy0 - y0, 1),
            (dx0 + dlx, dy0, A_WATER_Z, x1 - (dx0 + dlx), y1 - dy0, 1)]


# ---------------------------------------------------------------------------
# 水面参考对象（半透明，Z 可单独调整）
# ---------------------------------------------------------------------------
def parts_water():
    g = '13_Water_Surface_Reference'
    w = a_water_pieces()
    return [
        P(g, 'A_Water_Surface', w[0][0], w[0][1], A_WATER_Z, A_TANK_X - 2 * WALL,
          A_TANK_Y - 2 * WALL, 1, boxes=w, k='water', col='water'),
        P(g, 'B_Water_Surface_S3', B_BASIN[0], B_BASIN[1], B_WATER_S3_Z,
          B_BASIN[2], B_BASIN[3], 1, k='water', col='water',
          cut=[(B_MOUND[0], B_MOUND[1], B_MOUND[2], B_MOUND[3])]),
        P(g, 'B_Water_Surface_S2', B_S2AREA[0], B_S2AREA[1], B_WATER_S2_Z,
          B_S2AREA[2], B_S2AREA[3], 1, k='water', col='water'),
        P(g, 'C_Tray_Water_Surface', 81, 193, BASE_T + ROAD_T + FLOOR_T + C_TRAY_WATER_LEVEL,
          214, 56, 1, k='water', col='water'),
        P(g, 'Recovery_Tank_Water_Surface', 303, 28, BASE_T + FLOOR_T + TANK_WATER_LEVEL,
          94, 64, 1, k='water', col='water'),
    ]


def all_parts():
    o = [P('01_Base', 'BasePlate', 0, 0, 0, BASE_L, BASE_W, BASE_T, col='base')]
    o += parts_A() + parts_B() + parts_C() + parts_D() + parts_E() + parts_F() + parts_G()
    o += parts_sensors() + parts_hoses() + parts_paths() + parts_water() + parts_cabling()
    return o


# ---------------------------------------------------------------------------
# 空间检查（包围盒）
# ---------------------------------------------------------------------------
# 设计意图内的接触/穿透：不算碰撞
EXEMPT = [
    ('A_Deep_Water_Tank', 'A_Tank_Inlet_Port', '接口穿壁（设计意图）'),
    ('A_Deep_Water_Tank', 'A_Tank_Drain_Port', '接口穿壁（设计意图）'),
    ('A_Deep_Water_Tank', 'A_Tank_Overflow_Port', '接口穿壁（设计意图）'),
    ('A_Deep_Water_Tank', 'A_Tank_Suction_Port', '接口穿壁（设计意图）'),
    ('A_Deep_Water_Tank', 'A_Water_Surface', '水面在槽内（设计意图）'),
    ('A_Deep_Water_Tank', 'Dormitory_Model', '槽底板挖去宿舍基座占位（宿舍即为西/北坑壁）'),
    ('A_Deep_Water_Tank', 'A_Zone_Apron', '门前地坪与坑壁相接（同一开口）'),
    ('A_Deep_Water_Tank', 'A_Tank_Drain_Adjuster', '调节板贴坑壁（设计意图）'),
    ('A_Zone_Apron', 'A_Tank_Drain_Port', '排水口穿过地坪侧壁（按图钻孔）'),
    ('A_Zone_Apron', 'Dormitory_Model', '散水贴宿舍外墙（设计意图）'),
    ('A_Zone_Apron', 'C_Main_Road', '地坪与主路顺接（同一标高带）'),
    ('A_Zone_Apron', 'C_Connector_Road', '地坪与 A/B 连接路顺接'),
    ('A_Zone_Apron', 'B_Woodland_Base', '地坪贴 B 区地形板边（分界处）'),
    ('A_Deep_Water_Tank', 'Sensor_S1', 'S1 支架夹持槽壁、探头入槽'),
    ('A_Water_Surface', 'Sensor_S1', 'S1 探头插入水面测深（设计意图）'),
    ('A_Water_Surface', 'Hose_Suction_1', '吸水管口没入水面（设计意图）'),
    ('B_Woodland_Base', 'B_Raised_Mound', '地形起伏（已开槽，凹坑内凸台）'),
    ('B_Woodland_Base', 'B_Water_Surface_S3', '水面在槽内（设计意图）'),
    ('B_Woodland_Base', 'B_Inlet_Port', '接口穿壁（设计意图）'),
    ('B_Woodland_Base', 'B_Drain_Port', '接口穿壁（设计意图）'),
    ('B_Woodland_Base', 'B_Suction_Port', '接口穿壁（设计意图）'),
    ('B_Woodland_Base', 'Sensor_S2', '传感器立于槽底'),
    ('B_Woodland_Base', 'Sensor_S3', '传感器立于槽底'),
    ('B_Woodland_Base', 'B_Water_Surface_S2', '水面在低洼内（设计意图）'),
    ('B_Raised_Mound', 'B_Water_Surface_S3', '水面已按凸台开缺口'),
    ('C_Road_Water_Tray', 'C_Tray_Water_Surface', '水面在盘内（设计意图）'),
    ('C_Road_Water_Tray', 'C_Tray_Inlet_Port', '接口穿壁（设计意图）'),
    ('C_Road_Water_Tray', 'C_Tray_Drain_Port', '接口穿壁（设计意图）'),
    ('Recovery_Tank', 'Recovery_Tank_Water_Surface', '水面在箱内（设计意图）'),
    ('Recovery_Tank', 'Recovery_Tank_Inlet_Port', '接口穿壁（设计意图）'),
    ('Recovery_Tank', 'Recovery_Tank_Drain_Port', '接口穿壁（设计意图）'),
    ('Recovery_Tank', 'Recovery_Tank_Overflow_Port', '接口穿壁（设计意图）'),
    ('Recovery_Tank', 'Recovery_Tank_Level_Window', '液位观察窗贴壁安装'),
    ('Linux_Main_Controller_Box', 'Linux_Mainboard_Placeholder', '主板置于盒内'),
    ('MCU_Sensor_Node_Box', 'MCU_Sensor_Board', '开发板置于盒内'),
    ('MCU_Pump_Node_Box', 'MCU_Pump_Board', '开发板置于盒内'),
    ('Flow_Sensor_Block', 'Pump_Suction_Port', '流量计卡装于吸水管'),
    ('Pump_Body', 'Pump_Suction_Port_Alt', '备用吸水口自泵体引出'),
    ('Hose_Suction_1', 'Pump_Suction_Port', '软管插入接口'),
    ('Hose_Suction_1', 'A_Tank_Suction_Port', '软管插入接口'),
    ('Hose_Suction_1', 'A_Water_Surface', '软管跨越水面之上'),
    ('Hose_Suction_2', 'Pump_Suction_Port_Alt', '软管插入接口'),
    ('Hose_Suction_2', 'B_Suction_Port', '软管插入接口'),
    ('Hose_Drain', 'Pump_Discharge_Port', '软管插入接口'),
    ('Hose_Drain', 'Recovery_Tank_Inlet_Port', '软管插入接口'),
    ('Sensor_S2', 'B_Water_Surface_S2', '探头穿过水面（设计意图）'),
    ('Sensor_S2', 'B_Water_Surface_S3', 'S3 水面已挖去低洼区，S2 立于低洼内'),
    ('Sensor_S3', 'B_Water_Surface_S3', 'S3 水面已挖去低洼区，探头穿水面'),
    ('Sensor_S1', 'A_Water_Surface', '探头穿过水面（设计意图）'),
    ('A_Tank_Inlet_Port', 'A_Water_Surface', '进水口与水面相接（设计意图）'),
    ('A_Tank_Drain_Port', 'A_Tank_Drain_Adjuster', '可调排水口滑板（设计意图）'),
    ('A_Tank_Drain_Adjuster', 'A_Water_Surface', '调水位滑板立于水中（设计意图）'),
    ('A_Tank_Suction_Port', 'A_Water_Surface', '吸水口位于水面高度（设计意图）'),
    ('A_Water_Surface', 'Bicycle_Parking', '自行车停放台面 21 被水面 22 漫过 1 mm（设计意图）'),
    ('A_Water_Surface', 'Bike_Placeholder_01', '自行车占位块穿过水面（水漫过自行车）'),
    ('A_Water_Surface', 'Bike_Placeholder_02', '自行车占位块穿过水面（水漫过自行车）'),
    ('A_Water_Surface', 'Bike_Placeholder_03', '自行车占位块穿过水面（水漫过自行车）'),
    ('C_Tray_Drain_Port', 'C_Tray_Water_Surface', '排水口与水面相接（设计意图）'),
    ('Recovery_Tank_Inlet_Port', 'Recovery_Tank_Water_Surface', '进水口与水面相接'),
    ('Recovery_Tank_Drain_Port', 'Recovery_Tank_Drain_Handle', '排空阀手柄（设计意图）'),
    ('Flow_Sensor_Block', 'Hose_Suction_1', '软管插入流量计（设计意图）'),
    ('B_Water_Surface_S3', 'B_Water_Surface_S2', 'S3 水面已挖去低洼区，两片水面不重叠'),
    # ---- V1.3 走线：线槽与线缆的设计接触 ----
    ('P3_Candidate_Stop', 'Cable_Duct_Trunk_S', '线槽跨过候选停靠标线（标线仅 1 mm 厚）'),
    ('Electronics_Zone_Curb', 'Cable_Duct_Pad', '垫内走线槽贴挡水圈内侧（挡水圈北带已开 74 mm 出线缺口）'),
    ('Linux_Main_Controller_Box', 'Cable_Linux_MCU_Sensor', '线缆经盒壁开孔出线（设计意图）'),
    ('Linux_Main_Controller_Box', 'Cable_Linux_MCU_Pump', '线缆经盒壁开孔出线（设计意图）'),
    ('MCU_Sensor_Node_Box', 'Cable_Linux_MCU_Sensor', '线缆经盒壁开孔出线（设计意图）'),
    ('MCU_Sensor_Node_Box', 'Cable_MCU_Sensor_S1', '线缆经盒壁开孔出线（设计意图）'),
    ('MCU_Sensor_Node_Box', 'Cable_MCU_Sensor_S2', '线缆经盒壁开孔出线（设计意图）'),
    ('MCU_Sensor_Node_Box', 'Cable_MCU_Sensor_S3', '线缆经盒壁开孔出线（设计意图）'),
    ('MCU_Pump_Node_Box', 'Cable_Linux_MCU_Pump', '线缆经盒壁开孔出线（设计意图）'),
    ('MCU_Pump_Node_Box', 'Cable_MCU_Pump_Pump', '线缆经盒壁开孔出线（设计意图）'),
    ('Pump_Controller_Connector', 'Cable_MCU_Pump_Pump', '线缆插入泵控制器接口（设计意图）'),
    ('Sensor_S1', 'Cable_MCU_Sensor_S1', '线缆进入 S1 底座接线腔'),
    ('Sensor_S2', 'Cable_MCU_Sensor_S2', '线缆进入 S2 底座接线腔'),
    ('Sensor_S3', 'Cable_MCU_Sensor_S3', '线缆进入 S3 底座接线腔'),
    ('B_Woodland_Base', 'Cable_MCU_Sensor_S2', '线缆下潜进入 S2 低洼（地形板此处已下沉开槽）'),
    ('B_Woodland_Base', 'Cable_MCU_Sensor_S3', '线缆下潜进入 S3 浅槽（地形板此处已下沉开槽）'),
    ('B_Water_Surface_S2', 'Cable_MCU_Sensor_S2', '线缆与 S2 探头同处穿水面'),
    ('B_Water_Surface_S3', 'Cable_MCU_Sensor_S3', '线缆与 S3 探头同处穿水面'),
]
_EX = {}
for _a, _b, _r in EXEMPT:
    _EX[frozenset((_a, _b))] = _r


def bb(p):
    return (p['x'], p['y'], p['z'], p['x'] + p['lx'], p['y'] + p['ly'], p['z'] + p['lz'])


def _ov(a, b, tol=0.5):
    return (min(a[3], b[3]) - max(a[0], b[0]) > tol and
            min(a[4], b[4]) - max(a[1], b[1]) > tol and
            min(a[5], b[5]) - max(a[2], b[2]) > tol)


def prims(p):
    """把一个逻辑对象拆成若干分件包围盒，避免 L 形/环带/树冠的粗包围盒误报。"""
    n, k = p['n'], p.get('k')
    if k in ('hose', 'cable'):
        pts, r = p['pts'], p['r']
        out = []
        for i in range(len(pts) - 1):
            a, b = pts[i], pts[i + 1]
            out.append((n, (min(a[0], b[0]) - r, min(a[1], b[1]) - r, min(a[2], b[2]) - r,
                            max(a[0], b[0]) + r, max(a[1], b[1]) + r, max(a[2], b[2]) + r)))
        return out
    if k == 'ring':
        b = p['band']
        x0, y0, z0 = p['x'], p['y'], p['z']
        x1, y1, z1 = x0 + p['lx'], y0 + p['ly'], z0 + p['lz']
        north = []
        if 'gap' in p:                       # 北带有出线缺口（线缆从此处穿出）
            gx, gw = p['gap']
            if gx > x0:
                north.append((n, (x0, y1 - b, z0, gx, y1, z1)))
            if gx + gw < x1:
                north.append((n, (gx + gw, y1 - b, z0, x1, y1, z1)))
        else:
            north.append((n, (x0, y1 - b, z0, x1, y1, z1)))
        return north + [(n, (x0, y0, z0, x1, y0 + b, z1)),
                        (n, (x0, y0 + b, z0, x0 + b, y1 - b, z1)),
                        (n, (x1 - b, y0 + b, z0, x1, y1 - b, z1))]
    if 'notch' in p:
        nx, ny, nlx = p['notch']
        x0, y0, z0 = p['x'], p['y'], p['z']
        x1, y1, z1 = x0 + p['lx'], y0 + p['ly'], z0 + p['lz']
        return [(n, (x0, y0, z0, x1, ny, z1)),
                (n, (x0, ny, z0, nx, y1, z1)),
                (n, (nx + nlx, ny, z0, x1, y1, z1))]
    if 'tree' in p:
        tx, ty, fl = p['tree']
        return [(n, (tx - 7, ty - 7, fl, tx + 7, ty + 7, fl + 20)),
                (n, (tx - 22, ty - 22, fl + 10, tx + 22, ty + 22, fl + 54))]
    if 'boxes' in p:
        return [(n, (b[0], b[1], b[2], b[0] + b[3], b[1] + b[4], b[2] + b[5])) for b in p['boxes']]
    return [(n, bb(p))]


def _soft_pair(a, b):
    """敷设层规则：线缆之间、线缆与线槽之间按敷设关系处理，不判干涉。"""
    ka, kb = a.get('k'), b.get('k')
    return ((ka == 'cable' and kb in ('cable', 'duct')) or
            (kb == 'cable' and ka in ('cable', 'duct')))


def run_check():
    parts = [p for p in all_parts() if p.get('k') != 'wire']
    errs, ok_ex, seen = [], [], set()
    for p in parts:
        x0, y0, z0, x1, y1, z1 = bb(p)
        if x0 < -1e-6 or y0 < -1e-6 or z0 < -1e-6:
            errs.append('越界(负坐标): %s' % p['n'])
        if x1 > BASE_L + 1e-6 or y1 > BASE_W + 1e-6:
            errs.append('越界(超出底板): %s  x1=%.1f y1=%.1f' % (p['n'], x1, y1))
    for i in range(len(parts)):
        for j in range(i + 1, len(parts)):
            a, b = parts[i], parts[j]
            if _soft_pair(a, b):
                continue
            key = frozenset((a['n'], b['n']))
            for _, ba in prims(a):
                for _, bx in prims(b):
                    if not _ov(ba, bx):
                        continue
                    if key in _EX:
                        if key not in seen:
                            seen.add(key)
                            ok_ex.append((a['n'], b['n'], _EX[key]))
                        continue
                    if key in seen:
                        continue
                    seen.add(key)
                    ow = min(ba[3], bx[3]) - max(ba[0], bx[0])
                    oh = min(ba[4], bx[4]) - max(ba[1], bx[1])
                    oz = min(ba[5], bx[5]) - max(ba[2], bx[2])
                    errs.append('干涉: %s <-> %s  重叠 %.1f x %.1f x %.1f mm' %
                                (a['n'], b['n'], ow, oh, oz))
    return errs, ok_ex


def report():
    parts = all_parts()
    lines = ['# 实验台组件坐标表（单位 mm，原点=底板左下角外侧底面）', '',
             '| 分组 | 对象 | X | Y | Z | 长(lx) | 宽(ly) | 高(lz) | 备注 |',
             '|---|---|---:|---:|---:|---:|---:|---:|---|']
    for p in parts:
        k = p.get('k', '')
        if k == 'tank':
            note = '开口水槽 壁%.0f/底%.0f' % (p['wall'], p['floor_t'])
        elif k == 'tankasm':
            note = '浅坑槽体 底3/路缘15/墙35（含缓坡）'
        elif k == 'apron':
            note = '门前地坪 厚%.0f（%d 块）' % (p['lz'], len(p['boxes']))
        elif k == 'ring':
            note = '环带 带宽%.0f' % p['band']
        elif k == 'hose':
            note = '软管折线 R%.0f' % p['r']
        elif k == 'duct':
            note = ('出线套 实心' if p.get('solid')
                    else 'U 形线槽 壁%.1f（两端开口）' % CABLE_DUCT_T)
        elif k == 'cable':
            note = '线缆折线 R%.0f（敷设层）' % p['r']
        elif k == 'wire':
            note = '虚线示意 %d 段' % (len(p['pts']) - 1)
        elif k == 'water':
            note = '半透明水面 Z 可调'
        elif k == 'terrain':
            note = '草坪地形板（开槽+低洼+凸台）'
        else:
            note = ''
        lines.append('| %s | %s | %.0f | %.0f | %.0f | %.0f | %.0f | %.0f | %s |' %
                     (p['g'], p['n'], p['x'], p['y'], p['z'], p['lx'], p['ly'], p['lz'], note))
    errs, ok_ex = run_check()
    solid = [p for p in parts if p.get('k') != 'wire' and p['n'] != 'BasePlate']
    xs0 = min(bb(p)[0] for p in solid)
    ys0 = min(bb(p)[1] for p in solid)
    xs1 = max(bb(p)[3] for p in solid)
    ys1 = max(bb(p)[4] for p in solid)
    zs1 = max(bb(p)[5] for p in solid)
    lines += ['', '## 空间检查结果', '',
              '- 实体内容包络：X %.0f~%.0f（%.0f mm），Y %.0f~%.0f（%.0f mm），最高 Z=%.0f' %
              (xs0, xs1, xs1 - xs0, ys0, ys1, ys1 - ys0, zs1),
              '- 底板 %.0f x %.0f x %.0f；余量 左%.0f / 右%.0f / 下%.0f / 上%.0f mm' %
              (BASE_L, BASE_W, BASE_T, xs0, BASE_L - xs1, ys0, BASE_W - ys1),
              '- 硬性干涉（未豁免）：**%d** 处' % len(errs)]
    for e in errs:
        lines.append('  - ' + e)
    lines.append('- 设计意图内接触/穿透：%d 处（已登记豁免原因）' % len(ok_ex))
    return '\n'.join(lines)


if __name__ == '__main__':
    txt = report()
    print(txt)
    with open('/home/jmp/text_to_cad/CAD/01_坐标表与空间检查.md', 'w') as f:
        f.write(txt + '\n')

