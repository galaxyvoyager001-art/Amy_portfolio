P = '/home/user/Amy_portfolio/portfolio/project/'
BG, CR, AC, OR = '#0E4D40', '#FFF3DE', '#7FE0C1', '#FF6B3D'
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
.stat{display:flex;flex-direction:column;gap:6px;border-top:2px solid #FF6B3D;padding-top:10px}
.sn{font-size:56px;line-height:.85;color:#FF6B3D}
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
items = [('01', 'Coupled pendulums, IYPT &amp; CYPT', 'IB Extended Essay · team captain', '15–16'),
         ('02', 'SmartHearing AI hearing aid', 'Peking University · patent', '17'),
         ('03', 'Metallic glass under impact', 'Chinese Academy of Sciences · first author', '18'),
         ('04', 'Curawave transfer mattress', 'Conrad Challenge · CTO', '19'),
         ('05', 'Lingtong, my startup', 'founder · trademarks · USD 100k+ raised', '20'),
         ('06', 'Experimental optics', 'Peking University · research intern', '21'),
         ('07', 'Modelling &amp; publishing', 'IMMC · HiMCM · journal editor', '22')]
lst = ''.join(f'''<div style="display: grid; grid-template-columns: 54px minmax(0, 1fr) 78px; gap: 12px; align-items: baseline; padding: 11px 0; border-top: 1px solid rgba(14,30,25,.18)">
<span class="d" style="font-size: 34px; line-height: .9; color: {OR}">{n}</span>
<div><div class="b" style="font-size: 17px; font-weight: 600; color: #0E1E19; line-height: 1.2">{t}</div><div class="m" style="font-size: 9.5px; letter-spacing: .08em; color: #5A6B66; padding-top: 3px">{v}</div></div>
<span class="m" style="font-size: 11px; color: #0E1E19; text-align: right">p. {p}</span></div>''' for n, t, v, p in items)
stats = [('1', 'patent for an AI hearing aid'), ('2', 'first-author research papers'), ('$100k+', 'raised for my startup'), ('3', 'modelling Finalist awards')]
st = ''.join(f'<div class="stat"><span class="d sn">{a}</span><span class="b sl">{b}</span></div>' for a, b in stats)
body = f"""<div style="width: 1920px; height: 960px; position: relative; overflow: hidden; background: {BG}; color: {CR}">
<div class="m" style="position: absolute; left: 56px; right: 56px; top: 36px; display: flex; justify-content: space-between; font-size: 12px; color: {AC}"><span>05 — Mind</span><span>Six research projects and a company · 2023–2026</span><span style="color: {CR}">Amy Hu · 14</span></div>
<div class="d" style="position: absolute; left: 50px; top: 82px; font-size: 120px; line-height: .87; color: {CR}">RESEARCH &amp;<br><span style="color: {AC}">ENTREPRE&shy;NEURSHIP</span></div>
<div class="s" style="position: absolute; left: 56px; top: 316px; width: 700px; font-size: 38px; line-height: 1.12; font-style: italic; color: {CR}">How do people sense the world, and what can I build when a sense fails?</div>
<div class="b" style="position: absolute; left: 56px; top: 444px; width: 680px; font-size: 16px; line-height: 1.55; color: #D6EBE4">From physics tournaments, where I captained my team, to laboratories at Peking University and the Chinese Academy of Sciences, and then to two assistive products and the company I founded to make them real. The next eight pages show each project through its paper or plan: the question, the method, the figures and my role.</div>
<div style="position: absolute; left: 56px; top: 566px; width: 680px; display: flex; gap: 16px; align-items: baseline"><span class="m" style="font-size: 11px; color: {AC}; white-space: nowrap">My role</span><span class="b" style="font-size: 14.5px; line-height: 1.5; color: {CR}">Team captain, first author, product designer and founder: I built the rigs, ran the experiments, wrote the papers and pitched the products.</span></div>
<div style="position: absolute; left: 56px; bottom: 54px; width: 680px; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px">{st}</div>

<div class="pol" style="left: 840px; top: 96px; width: 330px; transform: rotate(-4deg)"><img src="/_blob/2e1b9f50d4145ca72acfc87fa3a100bd" alt="Amy on stage as a Conrad Challenge finalist" style="display: block; width: 306px; height: 430px; object-fit: cover; object-position: 50% 22%"><div class="h" style="font-size: 26px; color: #1B1B1B; padding: 8px 4px 12px">on stage, Conrad Challenge</div></div>
<img class="stk" src="/_blob/0a03bdca882d35d68dd7b2cc9cb7f46f" alt="My 3D-printed magnetic pendulum rig" style="position: absolute; left: 790px; top: 650px; width: 380px; transform: rotate(3deg)">
<div class="h" style="position: absolute; left: 590px; top: 668px; font-size: 27px; color: #FFD9A8; transform: rotate(-5deg); width: 190px; line-height: 1.05; text-align: right">my 3D-printed pendulum chain, IYPT →</div>

<div style="position: absolute; left: 1250px; top: 104px; width: 610px; height: 760px; background: {CR}; transform: rotate(1.5deg); box-shadow: 0 22px 36px rgba(0,0,0,.35); padding: 34px 36px 24px; box-sizing: border-box">
<div style="position: absolute; left: 230px; top: -16px; width: 150px; height: 34px; background: rgba(255,214,120,.85); transform: rotate(-3deg)"></div>
<div style="display: flex; justify-content: space-between; align-items: baseline"><span class="d" style="font-size: 44px; color: #0E1E19">IN THIS SECTION</span><span class="m" style="font-size: 11px; color: #5A6B66">p. 15 — 22</span></div>
<div style="padding-top: 10px">{lst}</div>
<div class="h" style="font-size: 25px; color: {OR}; padding-top: 14px; transform: rotate(-1deg)">two projects became one company →</div>
<img src="/_blob/78f7f49b8d10aecff86c08796220092f" alt="Lingtong logo" style="position: absolute; right: 40px; bottom: 26px; height: 92px; transform: rotate(-4deg)">
</div>
"""
open(P + 'Mind-Opener.dc.html', 'w').write(HEAD + body + TAIL)
