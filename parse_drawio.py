# -*- coding: utf-8 -*-
"""解析 drawio，导出 drawio 原始几何（px），用于与 layout_params.py 交叉校核。"""
import xml.etree.ElementTree as ET
import glob
import re
import sys

f = glob.glob('/home/jmp/text_to_cad/CAD/*.drawio')[0]
root = ET.parse(f).getroot()
page = root[0]
model = page.find('mxGraphModel')
cells = model.find('root')

rows = []
for c in cells:
    g = c.find('mxGeometry')
    if g is None:
        continue
    try:
        x = float(g.get('x', 0)); y = float(g.get('y', 0))
        w = float(g.get('width', 0)); h = float(g.get('height', 0))
    except (TypeError, ValueError):
        continue
    label = c.get('value') or ''
    label = re.sub(r'<[^>]+>', ' ', label)
    label = label.replace('&nbsp;', ' ').replace('&amp;', '&')
    label = re.sub(r'\s+', ' ', label).strip()
    style = c.get('style') or ''
    fill = ''
    m = re.search(r'fillColor=(#[0-9a-fA-F]{6})', style)
    if m:
        fill = m.group(1)
    if w <= 0 or h <= 0:
        continue
    rows.append((c.get('id'), label, x, y, w, h, fill))

rows.sort(key=lambda r: (round(r[3] / 20), r[2]))

print('%-6s %-42s %7s %7s %7s %7s %8s' % ('id', 'label', 'x', 'y', 'w', 'h', 'fill'))
for r in rows:
    print('%-6s %-42s %7.1f %7.1f %7.1f %7.1f %8s' % (r[0], r[1][:42], r[2], r[3], r[4], r[5], r[6]))

xs0 = min(r[2] for r in rows); ys0 = min(r[3] for r in rows)
xs1 = max(r[2] + r[4] for r in rows); ys1 = max(r[3] + r[5] for r in rows)
print('\ncontent bbox: x %.1f..%.1f (%.1f)  y %.1f..%.1f (%.1f)  ratio=%.3f'
      % (xs0, xs1, xs1 - xs0, ys0, ys1, ys1 - ys0, (xs1 - xs0) / (ys1 - ys0)))
