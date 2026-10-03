exec(open('/tmp/claude-0/-home-user-Amy-portfolio/2b4f3ce3-d4ad-5be4-9b15-7ee08bf2127f/scratchpad/m8common.py').read())
DK = '#14211C'
E = [('01', '#E8333A', 'p. 15–16', 'Energy Transport and Localization in a Chain of Magnetically Coupled Pendulums', 'IB Extended Essay · IYPT Macao team captain · CYPT 2026',
      'A Lagrangian model built from measured parameters reproduced the normal-mode frequencies within about 1.4%; two further CYPT problems, Electrical Damping and Levitation Control, follow.', '65f30f882333e620f82d5f8abdffdf71', 'contain'),
     ('02', '#E86A4A', 'p. 17', 'SmartHearing: Scene-Adaptive Hearing Assistance via LALM-Guided Sound Enhancement', 'Peking University, Institute for AI · patent · co-first author',
      'Which sound matters most depends on the scene. In a 101-participant listening test the system was rated most salient in 50.5% of trials.', 'a4a5ad7be8959db013341505f730570e', 'cover'),
     ('03', '#D9822B', 'p. 18', 'Flowed Metal: Micro-particle Impacts on Metallic Glasses under High Temperature', 'Chinese Academy of Sciences, Institute of Mechanics · first author · ISEF Beijing',
      'Laser-launched particles at 25, 100 and 200 °C: a ~10.4% fall in dynamic yield strength shows the glass softens and flows when hot.', 'd5cdc3ff88631e74d766faf945a07264', 'cover'),
     ('04', '#2EA39A', 'p. 19–20', 'Curawave: A Wave-Bionic Soft Robotic Mattress, and the Company Behind It', 'Conrad Challenge · founder of Beijing Lingtong Future Technology',
      'Silicone units tilt left and right in alternating groups, sliding a patient sideways onto another bed. My startup raised over USD 100k.', '9d8e6e3557fbd85611fe80cffbd26e34', 'cover'),
     ('05', '#4FA36B', 'p. 21', 'Polarisation Control and Experimental Optics', 'Peking University, Institute of Physics · nonlinear optics intern',
      'Twelve optics experiments written up as full lab reports, then Raman and laser systems and more than twenty polarisation states.', 'c7f14c186342008a33a753759401268f', 'cover'),
     ('06', '#C9A227', 'p. 22', 'Mathematical Modelling and Science Publishing', 'IMMC · HiMCM · team captain and main modeller · journal editor',
      'Five papers, all written by me, three Finalist awards; and an editor of our school\'s mathematics journal.', 'c2ec89f47e3ad9dc90c13dd2569ab178', 'cover')]
ROLES = ['I designed and 3D-printed the rig, built the Lagrangian model, and led the team as captain.', 'Equal-contribution author: I led the hearing-aid product design and hold its patent.', 'First author: I prepared the samples, ran every impact test and built the FEM simulation.', 'Founder and CTO: moulds, silicone casting, valves and Arduino control; trademark filed for the company.', 'I aligned every set-up myself and wrote all twelve reports with full error analysis.', 'Team captain and main modeller: I split each problem, built the core models and wrote the papers.']
cards = ''
for i, (n, c, pg, t, meta, d, img, fit) in enumerate(E):
    x = 56 + (i % 3) * 616; y = 336 + (i // 3) * 300
    bg = '#FFFFFF' if fit == 'contain' else '#DDD6C8'
    cards += f'''<div style="position: absolute; left: {x}px; top: {y}px; width: 576px; height: 270px; display: grid; grid-template-columns: 200px minmax(0, 1fr); gap: 18px; border-top: 4px solid {c}; padding-top: 12px; box-sizing: border-box">
<div style="height: 246px; background: {bg}; overflow: hidden"><img src="/_blob/{img}" alt="{t}" style="width: 100%; height: 100%; object-fit: {fit}; display: block"></div>
<div style="display: flex; flex-direction: column; gap: 5px">
<div style="display: flex; justify-content: space-between; align-items: baseline"><span class="pf" style="font-size: 44px; line-height: .9; font-weight: 900; color: {c}">{n}</span><span class="m" style="font-size: 11px; color: {DK}">{pg}</span></div>
<div class="pf" style="font-size: 17.5px; line-height: 1.16; font-weight: 700; color: {DK}">{t}</div>
<div class="m" style="font-size: 9px; line-height: 1.4; letter-spacing: .06em; color: {c}">{meta}</div>
<div class="sr" style="font-size: 13px; line-height: 1.42; color: #3A4440; text-align: justify">{d}</div>
<div class="sr" style="margin-top: auto; border-left: 3px solid {c}; padding-left: 10px; font-size: 12.5px; line-height: 1.4; font-style: italic; color: {DK}"><b style="font-style: normal">My role.</b> {ROLES[i]}</div>
</div></div>
'''
lines = ''.join(f'<line x1="{1150 + k * 26}" y1="0" x2="{1150 + k * 26 - 260}" y2="280" stroke="rgba(232,176,74,.10)" stroke-width="1.2"/>' for k in range(32))
body = f"""<div style="position: absolute; left: 0; top: 0; width: 1920px; height: 304px; background: {DK}; overflow: hidden"><svg width="1920" height="304" viewBox="0 0 1920 304" style="position: absolute; left: 0; top: 0" aria-hidden="true">{lines}</svg></div>
<div class="m" style="position: absolute; left: 56px; top: 34px; right: 56px; display: flex; justify-content: space-between; font-size: 11px; color: #E8B04A"><span>05 — Mind · Research &amp; leadership · six projects and a startup, 2023–2026</span><span style="color: #FFFFFF">Amy Hu · 14</span></div>
<div style="position: absolute; left: 56px; top: 70px; width: 820px; color: #FFFFFF">
<div class="pf" style="font-size: 50px; line-height: 1.02; font-weight: 900">Research Portfolio: <span style="color: #E8B04A; font-style: italic">Physics, Acoustics, Materials and Assistive Engineering</span></div></div>
<div class="sr" style="position: absolute; left: 930px; top: 74px; width: 934px; column-count: 2; column-gap: 30px; font-size: 14px; line-height: 1.5; color: #D9E2DC; text-align: justify; border-top: 1px solid rgba(255,255,255,.4); padding-top: 10px">My research asks the same question as the rest of this portfolio: how do people sense the world, and what can engineering do when a sense fails or a body is fragile? It runs from physics tournaments, where I captained my team, through laboratories at Peking University and the Chinese Academy of Sciences, to two assistive products and the company I founded to build them. Each entry below gives the paper's title, where the work was done, my role, and a summary drawn from its abstract; the pages that follow show the papers themselves.</div>
""" + kws([('1', 'patent, AI hearing aid'), ('2', 'first-author research papers'), ('$100k+', 'raised for my startup'), ('ISEF', 'Beijing qualifier'), ('IYPT', 'Macao team captain'), ('3', 'modelling Finalist awards')], 930, 934, 0, col='#FFFFFF', top=196) + cards
write('Mind-Opener.dc.html', 'Research', PAPER, body)
