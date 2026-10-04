P = '/home/user/Amy_portfolio/portfolio/project/'
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Research &amp; Entrepreneurship</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&amp;family=Instrument+Serif:ital@0;1&amp;family=Instrument+Sans:wght@400;500;600;700&amp;family=Caveat:wght@500;700&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">
<style>
body{margin:0}
.d{font-family:'Bricolage Grotesque','Arial Narrow',sans-serif;font-variation-settings:'wdth' 75;font-weight:800;letter-spacing:-.02em}
.s{font-family:'Instrument Serif',Georgia,serif}
.b{font-family:'Instrument Sans','Helvetica Neue',sans-serif}
.m{font-family:'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase}
.h{font-family:'Caveat',cursive;font-weight:700}
.stk{filter:drop-shadow(5px 0 0 #fff) drop-shadow(-5px 0 0 #fff) drop-shadow(0 5px 0 #fff) drop-shadow(0 -5px 0 #fff) drop-shadow(0 22px 26px rgba(0,0,0,.4))}
.stat{display:flex;flex-direction:column;gap:6px;border-top:2px solid #FF5A1F;padding-top:10px}
.sn{font-size:52px;line-height:.85;color:#FF5A1F}
.sl{font-size:13.5px;line-height:1.35}
.pol{position:absolute;background:#FFFDF8;padding:12px 12px 0;box-sizing:border-box;box-shadow:0 18px 30px rgba(0,0,0,.4)}
</style>
</helmet>
"""
TAIL = """</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1920,"height":960}}'>
class Component extends DCLogic {
renderVals() {
return {};
}
}
</script>
</body>
</html>
"""

INK, PAPER, OR, BL = '#141414', '#FFF3DE', '#FF5A1F', '#3A55E2'
E = [('01', '#E8333A', 'p. 15–16', 'Energy Transport in a Chain of Magnetically Coupled Pendulums', 'IB Extended Essay · IYPT &amp; CYPT team captain', 'f208c647069e9343412650e08270708f'),
     ('02', '#E86A4A', 'p. 17', 'SmartHearing: Scene-Adaptive Hearing Assistance', 'Peking University, Institute for AI · patent', 'b195f726cdf3314f3b56532febafa2b7'),
     ('03', '#D9822B', 'p. 18', 'Micro-particle Impacts on Metallic Glasses at High Temperature', 'Chinese Academy of Sciences · first author', 'd5cdc3ff88631e74d766faf945a07264'),
     ('04', '#2EA39A', 'p. 19–20', 'Curawave Transfer Mattress and the LingTong Startup', 'Conrad Challenge · founder &amp; CTO', '9d8e6e3557fbd85611fe80cffbd26e34'),
     ('05', '#4FA36B', 'p. 21', 'Polarisation Control and Experimental Optics', 'Peking University, Institute of Physics', 'c7f14c186342008a33a753759401268f'),
     ('06', '#C9A227', 'p. 22', 'Mathematical Modelling and Science Publishing', 'IMMC · HiMCM · 3 Finalist awards', 'c2ec89f47e3ad9dc90c13dd2569ab178')]
rot = [-2.2, 1.6, -1.0, 1.8, -1.6, 1.2]
cards = ''
for i, (n, c, pg, t, v, img) in enumerate(E):
    x = 760 + (i % 3) * 372; y = 92 + (i // 3) * 428
    cards += f"""<div style="position: absolute; left: {x}px; top: {y}px; width: 340px; background: #FFFFFF; padding: 12px 12px 14px; box-sizing: border-box; box-shadow: 0 14px 26px rgba(60,40,10,.18); transform: rotate({rot[i]}deg)">
<img src="/_blob/{img}" alt="{t}" style="width: 316px; height: 220px; object-fit: cover; display: block">
<div style="display: flex; justify-content: space-between; align-items: baseline; padding-top: 10px"><span class="d" style="font-size: 44px; line-height: .9; color: {c}">{n}</span><span class="m" style="font-size: 11px; color: {INK}">{pg}</span></div>
<div class="b" style="font-size: 17px; line-height: 1.22; font-weight: 600; color: {INK}; padding-top: 6px">{t}</div>
<div class="m" style="font-size: 9.5px; line-height: 1.45; letter-spacing: .07em; color: #6A6A6A; padding-top: 5px">{v}</div>
</div>
"""
stats = [('1', 'patent for an AI hearing aid'), ('2', 'first-author research papers'), ('$100k+', 'raised for my startup'), ('3', 'modelling Finalist awards')]
st = ''.join(f'<div class="stat"><span class="d sn">{a}</span><span class="b sl">{b}</span></div>' for a, b in stats)
body = f"""<div style="width: 1920px; height: 960px; position: relative; overflow: hidden; background: {PAPER}; color: {INK}">
<div class="m" style="position: absolute; left: 56px; top: 40px; font-size: 12px">05 — Mind · Research &amp; Entrepreneurship</div>
<div class="m" style="position: absolute; right: 56px; top: 40px; font-size: 12px">Amy Hu · 14</div>
<div class="d" style="position: absolute; left: 50px; top: 88px; font-size: 118px; line-height: .86; color: {INK}">RESEARCH &amp;<br><span style="color: {OR}">ENTREPRE&shy;NEURSHIP</span></div>
<div class="s" style="position: absolute; left: 56px; top: 312px; width: 640px; font-size: 32px; line-height: 1.12; font-style: italic">How do people sense the world, and what can engineering do when a sense fails?</div>
<div class="b" style="position: absolute; left: 56px; top: 412px; width: 410px; font-size: 15.5px; line-height: 1.55; color: #333">Six projects and one startup: from physics tournaments, where I captained my team, through laboratories at Peking University and the Chinese Academy of Sciences, to two assistive products and the company I founded to build them. Each of the next eight pages shows one of them through its paper.</div>
<div class="pol" style="left: 498px; top: 404px; width: 210px; transform: rotate(3deg); box-shadow: 0 14px 26px rgba(60,40,10,.22)"><img src="/_blob/2e1b9f50d4145ca72acfc87fa3a100bd" alt="Amy on stage as a Conrad Challenge finalist" style="display: block; width: 186px; height: 250px; object-fit: cover; object-position: 50% 20%"><div class="h" style="font-size: 21px; color: {INK}; padding: 6px 2px 10px">me, on stage</div></div>
<div style="position: absolute; left: 56px; bottom: 54px; width: 652px; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px">{st}</div>
{cards}"""
open(P + 'Mind-Opener.dc.html', 'w').write(HEAD + body + TAIL)
