exec(open('/tmp/claude-0/-home-user-Amy-portfolio/2b4f3ce3-d4ad-5be4-9b15-7ee08bf2127f/scratchpad/m8common.py').read())
PL, GD = '#33244D', '#E0A93B'
def ph(w, h, t, dark=False):
    c = 'rgba(255,255,255,.75)' if dark else '#B07A12'
    return f'<div style="box-sizing: border-box; width: {w}; height: {h}px; border: 1.5px dashed {c}; display: flex; align-items: center; justify-content: center; text-align: center; padding: 8px; font-family: \'IBM Plex Mono\',monospace; font-size: 10px; letter-spacing: .08em; text-transform: uppercase; color: {c}">{t}</div>'
def node(t, d, w='auto', hi=False):
    bg = GD if hi else 'rgba(255,255,255,.08)'
    col = PL if hi else '#FFFFFF'
    return f'<div style="flex: {w}; background: {bg}; border: 1px solid rgba(255,255,255,.35); padding: 9px 12px; color: {col}"><div class="lbl" style="font-size: 10.5px">{t}</div><div class="sr" style="font-size: 12.5px; line-height: 1.35; padding-top: 3px; opacity: .92">{d}</div></div>'
vline = '<div style="height: 18px; border-left: 1.5px solid rgba(255,255,255,.55); margin-left: 50%"></div>'
band = f"""<div style="position: absolute; left: 0; top: 262px; width: 1920px; height: 262px; background: {PL}"></div>
<div style="position: absolute; left: 56px; top: 280px; width: 1000px; display: flex; flex-direction: column">
<div class="m" style="font-size: 11px; color: {GD}; padding-bottom: 8px">How the company is organised</div>
<div style="display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 16px; align-items: stretch">
{node('Lingtong Future Technology', 'One shared R&amp;D team behind two product lines.', hi=True)}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px">
{node('Founder &amp; CTO · me', 'Technology, prototypes and patents for both products.')}
{node('CEO', 'Strategy, partners and the go-to-market plan.')}
{node('CFO', 'Budget, financial model and fundraising.')}
</div></div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; padding-top: 10px">
{node('R&amp;D lab', 'CAD, 3D printing, silicone casting, embedded control, audio AI.')}
{node('Testing', 'Listening tests; hospital trials and NMPA certification.')}
{node('Brand &amp; channels', 'Website, Bilibili, training videos, seminars.')}
{node('Finance', 'Angel round, subsidies, venture capital; 1% to charity.')}
</div></div>
<div style="position: absolute; left: 1100px; top: 280px; width: 764px; display: grid; grid-template-columns: 150px 150px minmax(0, 1fr); gap: 16px; color: #FFFFFF">
<img src="/_blob/a1291c76332a5509a971edfa752067f1" alt="Trademark registration application acceptance notice" style="width: 150px; height: 212px; object-fit: cover; object-position: top; display: block; background: #FFFFFF">
<img src="/_blob/e80017ff83f7156c3208b37ae73be68e" alt="Trademark preliminary approval and publication notice" style="width: 150px; height: 212px; object-fit: cover; object-position: top; display: block; background: #FFFFFF">
<div><div class="lbl" style="color: {GD}">Trademarks</div><div class="sr" style="font-size: 13px; line-height: 1.48; padding-top: 6px; color: #EDE6F7">Filed on 1 July 2026 with China\'s National Intellectual Property Administration (CNIPA). Application No. 92712127 (Class 42, scientific and technological services) was accepted on 20 July 2026. Application No. 92712148 passed preliminary examination and was published in Trademark Gazette No. 2001 on 27 September 2026.</div><div class="fcap" style="color: #C9BEDD; padding-top: 8px">Left: acceptance notice. Right: preliminary approval notice.</div></div>
</div>
"""
prods = f"""<div style="position: absolute; left: 56px; top: 548px; width: 600px">
<div class="lbl" style="color: {PL}; border-top: 3px solid {PL}; padding-top: 7px">Two product lines</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; padding-top: 10px">
<div><img src="/_blob/b195f726cdf3314f3b56532febafa2b7" alt="SmartHearing hearing-aid prototype in its charging case" style="width: 100%; height: 150px; object-fit: cover; display: block"><div class="pf" style="font-size: 17px; font-weight: 900; color: {INK}; padding-top: 7px">SmartHearing</div><div class="sr" style="font-size: 12.5px; line-height: 1.4; color: #333">AI hearing aid that hears the scene and enhances the sound that matters. Patent held; research paper on p. 17.</div></div>
<div><img src="/_blob/9d8e6e3557fbd85611fe80cffbd26e34" alt="Cast silicone Curawave units" style="width: 100%; height: 150px; object-fit: cover; display: block"><div class="pf" style="font-size: 17px; font-weight: 900; color: {INK}; padding-top: 7px">Curawave</div><div class="sr" style="font-size: 12.5px; line-height: 1.4; color: #333">Wave-bionic mattress that slides patients sideways from bed to bed. Working 1 × 4 prototype; p. 19.</div></div>
</div></div>"""
model = f"""<div style="position: absolute; left: 690px; top: 548px; width: 560px">
<div class="lbl" style="color: {PL}; border-top: 3px solid {PL}; padding-top: 7px">Business model</div>
<table class="tbl" style="margin-top: 8px; font-size: 11.5px">
<tr><td style="text-align: left; width: 110px"><b>Customers</b></td><td style="text-align: left">Hospitals (tier-1 first), care homes, people with hearing loss and their families</td></tr>
<tr><td style="text-align: left"><b>Channels</b></td><td style="text-align: left">Direct sales to hospitals, website and social media, seminars and free online training</td></tr>
<tr><td style="text-align: left"><b>Revenue</b></td><td style="text-align: left">Device sales, yearly maintenance, customisation and licensing</td></tr>
<tr><td style="text-align: left"><b>Spending</b></td><td style="text-align: left">R&amp;D 6.67% and marketing 4.44% of turnover each year; 1% to charity</td></tr>
<tr><td style="text-align: left"><b>Funding</b></td><td style="text-align: left">Angel investors (target ¥200–500k), government subsidies for medical innovation, then a ¥2M venture round</td></tr>
<tr><td style="text-align: left"><b>Forecast</b></td><td style="text-align: left">Curawave turnover ¥2.3M → ¥21.6M over five years</td></tr>
</table></div>"""
steps = [('Now', 'Prototypes built; hearing-aid patent; USD 100k+ raised'), ('1 year', 'Patent and NMPA certification for Curawave; clinical trials in 5 top hospitals'),
         ('2–3 years', '50 hospitals and care homes; international environmental standard'), ('3–5 years', 'Overseas markets; AI force sensing; technology licensing')]
road = ''.join(f'<div style="display: grid; grid-template-columns: 78px minmax(0, 1fr); gap: 10px; padding: 6px 0; border-bottom: 1px solid #D9D2C3"><span class="pf" style="font-size: 15px; font-weight: 900; color: {GD if i == 0 else PL}">{a}</span><span class="sr" style="font-size: 12.5px; line-height: 1.38; color: #333">{b}</span></div>' for i, (a, b) in enumerate(steps))
roadmap = f"""<div style="position: absolute; left: 1284px; top: 548px; width: 580px">
<div class="lbl" style="color: {PL}; border-top: 3px solid {PL}; padding-top: 7px">Roadmap &amp; funding</div>
<div style="padding-top: 4px">{road}</div></div>"""
top = f"""<div class="m" style="position: absolute; left: 56px; top: 34px; right: 56px; display: flex; justify-content: space-between; font-size: 11px; color: {PL}; border-bottom: 2px solid {INK}; padding-bottom: 6px"><span>05 — Mind · Research Nº 04 · the company</span><span>Amy Hu · 20</span></div>
<div style="position: absolute; left: 56px; top: 74px; width: 640px; display: flex; flex-direction: column; gap: 10px; color: {INK}">
<div class="pf" style="font-size: 35px; line-height: 1.05; font-weight: 900; white-space: nowrap">Beijing Lingtong <span style="color: {PL}; font-style: italic">Future Technology</span></div>
<div class="sr" style="font-size: 15px; line-height: 1.42; font-style: italic; color: #444"><b style="font-style: normal; color: {INK}">Mission.</b> Turn research on hearing and patient care into products that people can actually buy, use and trust.</div>
<div class="m" style="font-size: 10.5px; color: #555">Founded by Amy Hu · assistive technology · USD 100k+ raised</div>
</div>
<div class="abs" style="position: absolute; left: 740px; top: 78px; width: 760px; column-count: 2; column-gap: 28px; color: {INK}; border-top: 1px solid {INK}; padding-top: 8px; font-size: 13px"><b style="color: {PL}">Motivations</b> &nbsp;A paper proves an idea works; only a product reaches the person who needs it. Both of my engineering projects began with someone I know: my grandfather, who struggled to hear, and my own weeks on an injured leg. Research at Peking University and the Conrad Challenge gave us working prototypes, so I founded Beijing Lingtong Future Technology to carry them further. The company keeps one small R&amp;D team behind both products, so what we learn about sensors, control and testing on one is reused on the other. Each co-founder owns one side of the business, and every spending decision is checked against our five-year model. As founder and CTO, I lead the technology for both products and pitch them to investors and hospitals.</div>
<img src="/_blob/78f7f49b8d10aecff86c08796220092f" alt="Lingtong logo" style="position: absolute; left: 1600px; top: 70px; height: 172px; display: block">
"""
body = top + band + prods + model + roadmap + f'<div style="position: absolute; left: 690px; top: 752px; width: 1174px"><div class="lbl" style="color: {PL}; border-top: 1px solid {PL}; padding-top: 7px">The market we are building for</div><div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 22px; padding-top: 8px"><div><div class="pf" style="font-size: 26px; font-weight: 900; color: {PL}; line-height: 1">70 M</div><div class="sr" style="font-size: 12.5px; line-height: 1.35; color: #333; padding-top: 3px">people in China bedridden by injury (2024)</div></div><div><div class="pf" style="font-size: 26px; font-weight: 900; color: {PL}; line-height: 1">96.4 M</div><div class="sr" style="font-size: 12.5px; line-height: 1.35; color: #333; padding-top: 3px">surgical operations a year in China</div></div><div><div class="pf" style="font-size: 26px; font-weight: 900; color: {PL}; line-height: 1">¥120 bn</div><div class="sr" style="font-size: 12.5px; line-height: 1.35; color: #333; padding-top: 3px">Chinese medical-device market</div></div><div><div class="pf" style="font-size: 26px; font-weight: 900; color: {PL}; line-height: 1">1.5 bn</div><div class="sr" style="font-size: 12.5px; line-height: 1.35; color: #333; padding-top: 3px">people worldwide living with hearing loss (WHO)</div></div></div></div>' + kws([('$100k+', 'raised'), ('2', 'product lines, one R&amp;D team'), ('1', 'patent, AI hearing aid'), ('2', 'trademark applications, 2026'), ('5 → 50', 'hospitals: year 1 to year 3'), ('1%', 'of turnover to charity')], 56, 1808, 20)
write('Mind-Startup.dc.html', 'Lingtong startup', PAPER, body)
