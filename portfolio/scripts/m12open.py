exec(open('/tmp/claude-0/-home-user-Amy-portfolio/2b4f3ce3-d4ad-5be4-9b15-7ee08bf2127f/scratchpad/m8common.py').read())
import math
BG, GD, TX = '#12221D', '#E8B04A', '#D5E0DA'
CX, CY, RX, RY, R = 1290, 448, 440, 300, 78
N = [('01', '#E8333A', 'Energy Transport in a Chain of Magnetically Coupled Pendulums', 'IB Extended Essay · IYPT &amp; CYPT team captain', 'p. 15–16', 'f208c647069e9343412650e08270708f'),
     ('02', '#E86A4A', 'SmartHearing: Scene-Adaptive Hearing Assistance', 'Peking University, Institute for AI · patent', 'p. 17', 'b195f726cdf3314f3b56532febafa2b7'),
     ('03', '#D9822B', 'Micro-particle Impacts on Metallic Glasses at High Temperature', 'Chinese Academy of Sciences · first author', 'p. 18', 'd5cdc3ff88631e74d766faf945a07264'),
     ('04', '#2EA39A', 'Curawave Transfer Mattress and the LingTong Startup', 'Conrad Challenge · founder &amp; CTO', 'p. 19–20', '9d8e6e3557fbd85611fe80cffbd26e34'),
     ('05', '#4FA36B', 'Polarisation Control and Experimental Optics', 'Peking University, Institute of Physics', 'p. 21', 'c7f14c186342008a33a753759401268f'),
     ('06', '#C9A227', 'Mathematical Modelling and Science Publishing', 'IMMC · HiMCM · 3 Finalist awards', 'p. 22', 'c2ec89f47e3ad9dc90c13dd2569ab178')]
svg = f'<ellipse cx="{CX}" cy="{CY}" rx="{RX}" ry="{RY}" fill="none" stroke="rgba(232,176,74,.28)" stroke-width="1" stroke-dasharray="3 6"/>'
nodes = ''
for i, (n, c, t, v, pg, img) in enumerate(N):
    a = math.radians(-60 + 60 * i)
    x, y = CX + RX * math.cos(a), CY + RY * math.sin(a)
    svg += f'<line x1="{CX}" y1="{CY}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(232,176,74,.45)" stroke-width="1"/><circle cx="{x:.0f}" cy="{y:.0f}" r="{R + 7}" fill="none" stroke="{c}" stroke-width="2"/>'
    nodes += f'<div style="position: absolute; left: {x - R:.0f}px; top: {y - R:.0f}px; width: {2 * R}px; height: {2 * R}px; border-radius: 50%; overflow: hidden; background: #FFFFFF"><img src="/_blob/{img}" alt="{t}" style="width: 100%; height: 100%; object-fit: cover; display: block"></div>\n'
    if i == 0:
        tx, ty, ta = x + R + 24, y - 50, 'left'
    elif i == 5:
        tx, ty, ta = x - R - 294, y - 50, 'right'
    else:
        tx, ty, ta = x - 120, y + R + 14, 'left'
    nodes += f'''<div style="position: absolute; left: {tx:.0f}px; top: {ty:.0f}px; width: 270px; text-align: {ta}">
<div style="display: flex; align-items: baseline; gap: 10px; justify-content: {'flex-end' if ta == 'right' else 'flex-start'}"><span class="pf" style="font-size: 30px; line-height: 1; font-weight: 900; color: {c}">{n}</span><span class="m" style="font-size: 10.5px; color: {GD}">{pg}</span></div>
<div class="pf" style="font-size: 16.5px; line-height: 1.18; font-weight: 700; color: #FFFFFF; padding-top: 4px">{t}</div>
<div class="m" style="font-size: 9px; line-height: 1.45; letter-spacing: .06em; color: #9AA6B6; padding-top: 4px">{v}</div></div>
'''
centre = f'''<div style="position: absolute; left: {CX - 112}px; top: {CY - 112}px; width: 224px; height: 224px; border-radius: 50%; overflow: hidden; border: 3px solid {GD}; box-sizing: border-box"><img src="/_blob/2e1b9f50d4145ca72acfc87fa3a100bd" alt="Amy on stage as a Conrad Challenge finalist" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 18%; display: block"></div>
<div class="m" style="position: absolute; left: {CX - 120}px; top: {CY + 120}px; width: 240px; text-align: center; font-size: 9.5px; color: {GD}; background: {BG}; padding: 3px 0">Me, on stage at the Conrad Challenge</div>'''
stats = [('1', 'patent, AI hearing aid'), ('2', 'first-author papers'), ('$100k+', 'raised for my startup'), ('ISEF', 'Beijing qualifier'), ('IYPT', 'Macao team captain'), ('3', 'modelling Finalist awards')]
st = ''.join(f'<div style="border-top: 1px solid rgba(255,255,255,.25); padding-top: 8px"><div class="pf" style="font-size: 34px; line-height: 1; font-weight: 900; color: #FFFFFF">{a}</div><div class="b" style="font-size: 12px; line-height: 1.3; color: #9AA6B6; padding-top: 3px">{b}</div></div>' for a, b in stats)
body = f"""<svg width="1920" height="960" viewBox="0 0 1920 960" style="position: absolute; left: 0; top: 0" aria-hidden="true">{svg}</svg>
<div class="m" style="position: absolute; left: 56px; top: 36px; font-size: 11px; color: {GD}">05 — Mind · Research &amp; entrepreneurship · 2023–2026</div>
<div class="m" style="position: absolute; right: 56px; top: 36px; font-size: 11px; color: #FFFFFF">Amy Hu · 14</div>
<div style="position: absolute; left: 56px; top: 96px; width: 580px; display: flex; flex-direction: column; gap: 24px">
<div class="pf" style="font-size: 66px; line-height: 1; font-weight: 900; color: #FFFFFF">Research &amp;<br><span style="color: {GD}; font-style: italic">Entrepreneurship</span></div>
<div class="m" style="font-size: 11px; line-height: 1.6; color: #9AA6B6">Physics · Acoustics · Materials · Optics · Assistive engineering · Mathematics</div>
<div class="sr" style="font-size: 16px; line-height: 1.62; color: {TX}; text-align: justify">Six projects and one startup, all circling one question: how do people sense the world, and what can engineering do when a sense fails? They run from physics tournaments, where I captained my team, through laboratories at Peking University and the Chinese Academy of Sciences, to two assistive products and the company I founded to build them. Each of the next eight pages shows one of them through its paper: title, abstract, method, figures and my role.</div>
<div style="border-left: 3px solid {GD}; padding-left: 14px"><div class="sr" style="font-size: 19px; line-height: 1.4; font-style: italic; color: #FFFFFF">"Every project began with a person: my grandfather who could not hear the street, a patient who could not be moved, a team that needed a captain."</div><div class="m" style="font-size: 10px; color: #9AA6B6; padding-top: 8px">Read clockwise from 01 · each colour continues on its own page</div></div>
</div>
<div style="position: absolute; left: 56px; bottom: 44px; width: 580px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 22px 22px">{st}</div>
{centre}
{nodes}"""
write('Mind-Opener.dc.html', 'Research', BG, body)
