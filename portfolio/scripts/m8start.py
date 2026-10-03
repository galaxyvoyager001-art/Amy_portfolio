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
band = f"""<div style="position: absolute; left: 0; top: 252px; width: 1920px; height: 318px; background: {PL}"></div>
<div class="m" style="position: absolute; left: 56px; top: 268px; font-size: 11px; color: {GD}">How the company is organised</div>
<div style="position: absolute; left: 56px; top: 290px; width: 1808px; display: flex; flex-direction: column">
<div style="display: flex; justify-content: center"><div style="width: 560px">{node('Beijing Lingtong Future Technology', 'Assistive technology for people whose senses or bodies let them down: one shared R&amp;D team, two product lines.', hi=True)}</div></div>
{vline}
<div style="border-top: 1.5px solid rgba(255,255,255,.55); margin: 0 240px"></div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 30px; padding-top: 14px">
{node('Founder &amp; CTO · Amy Hu', 'Technology and products: hardware, AI and prototypes; patent holder for the AI hearing aid.')}
{node('CEO · Emily Feng', 'Strategy, hospital and industry partners, pitching and the go-to-market plan.')}
{node('CFO · Galatea Shang', 'Budget, five-year financial model, fundraising and charity commitments.')}
</div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; padding-top: 16px">
{node('R&amp;D lab', 'CAD, 3D printing and silicone casting; embedded control; audio AI with university mentors.')}
{node('Clinical &amp; user testing', 'Listening tests (101 participants so far); hospital trials and NMPA certification for the mattress.')}
{node('Brand &amp; channels', 'Curawave brand, website and Bilibili account; training videos and offline seminars.')}
{node('Finance &amp; funding', 'Angel round, government subsidies, then venture capital; 1% of turnover to charity.')}
</div>
</div>
"""
prods = f"""<div style="position: absolute; left: 56px; top: 598px; width: 600px">
<div class="lbl" style="color: {PL}; border-top: 3px solid {PL}; padding-top: 7px">Two product lines</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; padding-top: 10px">
<div>{ph('100%', 120, 'Photo · SmartHearing<br>hearing-aid prototype<br>(please upload)')}<div class="pf" style="font-size: 17px; font-weight: 900; color: {INK}; padding-top: 7px">SmartHearing</div><div class="sr" style="font-size: 12.5px; line-height: 1.4; color: #333">AI hearing aid that hears the scene and enhances the sound that matters. Patent held; research paper on p. 17.</div></div>
<div><img src="/_blob/9d8e6e3557fbd85611fe80cffbd26e34" alt="Cast silicone Curawave units" style="width: 100%; height: 120px; object-fit: cover; display: block"><div class="pf" style="font-size: 17px; font-weight: 900; color: {INK}; padding-top: 7px">Curawave</div><div class="sr" style="font-size: 12.5px; line-height: 1.4; color: #333">Wave-bionic mattress that slides patients sideways from bed to bed. Working 1 × 4 prototype; p. 19.</div></div>
</div></div>"""
model = f"""<div style="position: absolute; left: 690px; top: 598px; width: 560px">
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
roadmap = f"""<div style="position: absolute; left: 1284px; top: 598px; width: 580px">
<div class="lbl" style="color: {PL}; border-top: 3px solid {PL}; padding-top: 7px">Roadmap &amp; funding</div>
<div style="padding-top: 4px">{road}</div><div style="display: grid; grid-template-columns: 78px minmax(0, 1fr); gap: 10px; padding: 8px 0 0"><span class="lbl" style="color: {PL}; padding-top: 10px">Partners</span>{ph('100%', 44, 'Hospital / university / investor partners · please send')}</div></div>"""
top = f"""<div class="m" style="position: absolute; left: 56px; top: 34px; right: 56px; display: flex; justify-content: space-between; font-size: 11px; color: {PL}; border-bottom: 2px solid {INK}; padding-bottom: 6px"><span>05 — Mind · Research Nº 04 · the company</span><span>Amy Hu · 20</span></div>
<div style="position: absolute; left: 56px; top: 74px; width: 640px; display: flex; flex-direction: column; gap: 10px; color: {INK}">
<div class="pf" style="font-size: 35px; line-height: 1.05; font-weight: 900; white-space: nowrap">Beijing Lingtong <span style="color: {PL}; font-style: italic">Future Technology</span></div>
<div class="sr" style="font-size: 15px; line-height: 1.42; font-style: italic; color: #444"><b style="font-style: normal; color: {INK}">Mission.</b> Turn research on hearing and patient care into products that people can actually buy, use and trust.</div>
<div class="m" style="font-size: 10.5px; color: #555">Founded by Amy Hu · assistive technology · USD 100k+ raised</div>
</div>
<div class="abs" style="position: absolute; left: 740px; top: 78px; width: 760px; column-count: 2; column-gap: 28px; color: {INK}; border-top: 1px solid {INK}; padding-top: 8px; font-size: 13px"><b style="color: {PL}">Why a company</b> &nbsp;A paper proves an idea works; only a product reaches the person who needs it. Both of my engineering projects began with someone I know: my grandfather, who struggled to hear, and my own weeks on an injured leg. Research at Peking University and the Conrad Challenge gave us working prototypes, so I founded Beijing Lingtong Future Technology to carry them further. The company keeps one small R&amp;D team behind both products, so what we learn about sensors, control and testing on one is reused on the other. Each co-founder owns one side of the business, and every decision about spending is checked against the five-year model. As founder and CTO, I lead the technology for both products and pitch them to investors and hospitals.</div>
<div style="position: absolute; left: 1540px; top: 74px; width: 324px; display: flex; flex-direction: column; gap: 10px">
{ph('100%', 70, 'Company logo<br>(please upload)')}
{ph('100%', 82, 'Team photo · founders<br>(please upload)')}
</div>
"""
body = top + band + prods + model + roadmap + kws([('$100k+', 'raised'), ('2', 'product lines, one R&amp;D team'), ('1', 'patent, AI hearing aid'), ('3', 'co-founders'), ('5 → 50', 'hospitals: year 1 to year 3'), ('1%', 'of turnover to charity')], 56, 1808, 20)
write('Mind-Startup.dc.html', 'Lingtong startup', PAPER, body)
