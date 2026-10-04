exec(open('/tmp/claude-0/-home-user-Amy-portfolio/2b4f3ce3-d4ad-5be4-9b15-7ee08bf2127f/scratchpad/m8common.py').read())
DK, BGc = '#1B1B1B', '#F1ECE2'
E = [('01', '#D9432E', 'p. 15–16', 'Energy Transport and Localization in a Chain of Magnetically Coupled Pendulums', 'IB Extended Essay · IYPT Macao and CYPT 2026 team captain',
      'A Lagrangian model from measured parameters matched the normal-mode frequencies within 1.4%; plus two CYPT problems I reported.', 'f208c647069e9343412650e08270708f'),
     ('02', '#C2412D', 'p. 17', 'SmartHearing: Scene-Adaptive Hearing Assistance via LALM-Guided Sound Enhancement', 'Peking University, Institute for AI · patent · co-first author',
      'Hears the scene, decides which sound matters, and enhances it; rated most salient in 50.5% of 303 listening trials.', 'a4a5ad7be8959db013341505f730570e'),
     ('03', '#B5541E', 'p. 18', 'Flowed Metal: Micro-particle Impacts on Metallic Glasses under High Temperature', 'Chinese Academy of Sciences, Institute of Mechanics · first author · ISEF Beijing',
      'Laser-launched particles at 25–200 °C: a 10.4% drop in dynamic yield strength shows the glass softens and flows.', 'd5cdc3ff88631e74d766faf945a07264'),
     ('04', '#0F7C7A', 'p. 19–20', 'Curawave: A Wave-Bionic Soft Robotic Mattress, and the Company I Founded', 'Conrad Challenge · founder and CTO of Beijing Lingtong Future Technology',
      'Silicone units tilt in alternating groups to slide a patient onto another bed; the startup has raised over USD 100k.', '9d8e6e3557fbd85611fe80cffbd26e34'),
     ('05', '#2F7D4F', 'p. 21', 'Polarisation Control and Experimental Optics', 'Peking University, Institute of Physics · nonlinear optics research intern',
      'Twelve optics experiments as full lab reports, then Raman and laser systems and twenty polarisation states.', 'c7f14c186342008a33a753759401268f'),
     ('06', '#C8641E', 'p. 22', 'Mathematical Modelling and Science Publishing', 'IMMC · HiMCM · team captain and main modeller · journal editor',
      'Five papers, all written by me; three Finalist awards; an editor of our school\'s mathematics journal.', 'c2ec89f47e3ad9dc90c13dd2569ab178')]
rows = ''
for i, (n, c, pg, t, meta, d, img) in enumerate(E):
    rows += f'''<div style="display: grid; grid-template-columns: 120px minmax(0, 1fr) 470px 170px 74px; gap: 26px; align-items: center; height: 108px; border-top: 1px solid {DK if i == 0 else 'rgba(27,27,27,.25)'}">
<span class="pf" style="font-size: 76px; line-height: 1; font-weight: 900; color: {c}; letter-spacing: -.02em">{n}</span>
<div><div class="pf" style="font-size: 21px; line-height: 1.16; font-weight: 700; color: {DK}">{t}</div><div class="m" style="font-size: 9.5px; letter-spacing: .07em; color: {c}; padding-top: 6px">{meta}</div></div>
<div class="sr" style="font-size: 14px; line-height: 1.45; color: #444">{d}</div>
<img src="/_blob/{img}" alt="{t}" style="width: 170px; height: 88px; object-fit: cover; display: block">
<span class="m" style="font-size: 12px; color: {DK}; text-align: right">{pg}</span>
</div>
'''
body = f"""<div class="m" style="position: absolute; left: 56px; top: 36px; right: 56px; display: flex; justify-content: space-between; font-size: 11px; color: {DK}"><span>05 — Mind · Research &amp; leadership · 2023–2026</span><span>Amy Hu · 14</span></div>
<div class="pf" style="position: absolute; left: 50px; top: 58px; font-size: 150px; line-height: 1; font-weight: 900; color: {DK}; letter-spacing: -.03em">Research<span style="color: #D9432E">.</span></div>
<div style="position: absolute; left: 820px; top: 86px; width: 690px">
<div class="sr" style="font-size: 17px; line-height: 1.55; color: #333; text-align: justify">Six projects and one startup. They run from physics tournaments, where I captained my team, through laboratories at Peking University and the Chinese Academy of Sciences, to two assistive products and the company I founded to build them. Each of the next eight pages presents one of them through its paper: title, abstract, method, figures and my role.</div>
<div class="m" style="font-size: 10px; color: #777; padding-top: 12px">Physics · Acoustics · Materials · Optics · Assistive engineering · Mathematics</div></div>
<div style="position: absolute; left: 1554px; top: 72px; width: 310px"><img src="/_blob/b1d57a32fae921a361a0141bf275e539" alt="Amy reporting Electrical Damping at CYPT 2026" style="width: 310px; height: 172px; object-fit: cover; display: block"><div class="fcap">Reporting Electrical Damping, CYPT 2026.</div></div>
<div style="position: absolute; left: 56px; top: 286px; width: 1808px; display: flex; flex-direction: column">{rows}<div style="border-top: 1px solid {DK}"></div></div>
"""
write('Mind-Opener.dc.html', 'Research', BGc, body)
