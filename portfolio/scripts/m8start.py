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
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 10px; padding-top: 10px">
{node('Algorithms &amp; AI', 'Sound understanding, priority decisions, separation.')}
{node('Embedded &amp; hardware', 'Real-time audio, low power; valves and control.')}
{node('Product &amp; design', 'Wearable form, CAD, 3D printing, casting.')}
{node('Regulatory &amp; clinical', 'Device classification, safety, pilots.')}
{node('Business &amp; supply', 'Partners, ODM makers, channels.')}
</div></div>
<div style="position: absolute; left: 1100px; top: 280px; width: 764px; display: grid; grid-template-columns: 150px 150px minmax(0, 1fr); gap: 16px; color: #FFFFFF">
<img src="/_blob/a1291c76332a5509a971edfa752067f1" alt="Trademark registration application acceptance notice" style="width: 150px; height: 212px; object-fit: cover; object-position: top; display: block; background: #FFFFFF">
<img src="/_blob/e80017ff83f7156c3208b37ae73be68e" alt="Trademark preliminary approval and publication notice" style="width: 150px; height: 212px; object-fit: cover; object-position: top; display: block; background: #FFFFFF">
<div><div class="lbl" style="color: {GD}">Trademarks</div><div class="sr" style="font-size: 13px; line-height: 1.48; padding-top: 6px; color: #EDE6F7">Filed on 1 July 2026 with China\'s National Intellectual Property Administration (CNIPA). Application No. 92712127 (Class 42, scientific and technological services) was accepted on 20 July 2026. Application No. 92712148 passed preliminary examination and was published in Trademark Gazette No. 2001 on 27 September 2026.</div><div class="fcap" style="color: #C9BEDD; padding-top: 8px">Left: acceptance notice. Right: preliminary approval notice.</div></div>
</div>
"""
def colhead(x, w, t):
    return f'<div style="position: absolute; left: {x}px; top: 548px; width: {w}px"><div class="lbl" style="color: {PL}; border-top: 3px solid {PL}; padding-top: 7px">{t}</div>'
PS = 'class="sr" style="font-size: 12.5px; line-height: 1.42; color: #333"'
prods = colhead(56, 420, 'Two product lines') + f"""<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; padding-top: 9px">
<div><img src="/_blob/b195f726cdf3314f3b56532febafa2b7" alt="SmartHearing hearing-aid prototype in its charging case" style="width: 100%; height: 112px; object-fit: cover; display: block"><div class="pf" style="font-size: 16px; font-weight: 900; color: {INK}; padding-top: 6px">SmartHearing</div><div {PS}>Core product: an AI hearing system that decides which sound you need to hear. Patent filed; p. 17.</div></div>
<div><img src="/_blob/9d8e6e3557fbd85611fe80cffbd26e34" alt="Cast silicone Curawave units" style="width: 100%; height: 112px; object-fit: cover; display: block"><div class="pf" style="font-size: 16px; font-weight: 900; color: {INK}; padding-top: 6px">Curawave</div><div {PS}>Second growth curve: a wave-bionic transfer mattress, three prototype generations; p. 19.</div></div>
</div><div class="sr" style="font-size: 12.5px; line-height: 1.4; color: {PL}; padding-top: 8px; font-style: italic">Focus: 70–80% of resources go to SmartHearing for the first 18 months.</div></div>"""
streams = [('Own-brand devices', 'SmartHearing as device + app + long-term service; basic hearing never put behind a subscription.'),
           ('Institutional solutions', 'Hearing centres, care homes and hospitals: equipment, training and maintenance. The mattress is B2B only.'),
           ('Technology licensing', 'An Auditory Decision Engine SDK for earbuds, hearing aids and smart glasses.')]
model = colhead(516, 420, 'Business model · three revenue streams') + '<div style="padding-top: 6px">' + ''.join(f'<div style="display: grid; grid-template-columns: 26px minmax(0, 1fr); gap: 8px; padding: 6px 0; border-bottom: 1px solid #D9D2C3"><span class="pf" style="font-size: 20px; line-height: 1; font-weight: 900; color: {GD}">{i + 1}</span><div><b class="b" style="font-size: 12px; color: {INK}">{a}</b><div {PS}>{b}</div></div></div>' for i, (a, b) in enumerate(streams)) + f'<div {PS} style="padding-top: 6px"><b>First users:</b> active adults 50+ with mild-to-moderate hearing loss, often bought by their adult children.</div></div></div>'
model = model.replace(f'<div {PS} style="padding-top: 6px">', '<div class="sr" style="font-size: 12.5px; line-height: 1.42; color: #333; padding-top: 6px">')
steps = [('0–6 mo', 'Research prototype → wearable SmartHearing; final mattress prototype; device-classification advice.'),
         ('6–12 mo', 'Pilots with 100–300 users and 3–5 hearing, care or rehab partners; first paid B2B pilots.'),
         ('12–24 mo', 'Design freeze, registration path, supply chain and first paid sales.'),
         ('24–36 mo', 'National channels; licensing of the Auditory Decision Engine begins.')]
road = ''.join(f'<div style="display: grid; grid-template-columns: 72px minmax(0, 1fr); gap: 10px; padding: 6px 0; border-bottom: 1px solid #D9D2C3"><span class="pf" style="font-size: 14px; font-weight: 900; color: {GD if i == 0 else PL}">{a}</span><span {PS}>{b}</span></div>' for i, (a, b) in enumerate(steps))
roadmap = colhead(976, 420, 'Three-year plan') + f'<div style="padding-top: 4px">{road}</div>' + '<div style="padding-top: 10px"><div class="b" style="font-size: 11px; font-weight: 700; color: #33244D">Planning case: revenue, ¥ million (a target to plan against, not a promise)</div><div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 6px; align-items: end; height: 54px; padding-top: 6px"><div style="display: flex; flex-direction: column; align-items: center; justify-content: flex-end; height: 100%"><span class="b" style="font-size: 10.5px; color: #333">1.8</span><span style="width: 70%; height: 3px; background: #33244D"></span><span class="m" style="font-size: 9px; color: #666">Y1</span></div><div style="display: flex; flex-direction: column; align-items: center; justify-content: flex-end; height: 100%"><span class="b" style="font-size: 10.5px; color: #333">14.5</span><span style="width: 70%; height: 3px; background: #33244D"></span><span class="m" style="font-size: 9px; color: #666">Y2</span></div><div style="display: flex; flex-direction: column; align-items: center; justify-content: flex-end; height: 100%"><span class="b" style="font-size: 10.5px; color: #333">50</span><span style="width: 70%; height: 5px; background: #33244D"></span><span class="m" style="font-size: 9px; color: #666">Y3</span></div><div style="display: flex; flex-direction: column; align-items: center; justify-content: flex-end; height: 100%"><span class="b" style="font-size: 10.5px; color: #333">130</span><span style="width: 70%; height: 14px; background: #33244D"></span><span class="m" style="font-size: 9px; color: #666">Y4</span></div><div style="display: flex; flex-direction: column; align-items: center; justify-content: flex-end; height: 100%"><span class="b" style="font-size: 10.5px; color: #333">300</span><span style="width: 70%; height: 34px; background: #33244D"></span><span class="m" style="font-size: 9px; color: #666">Y5</span></div></div></div></div>'
alloc = [(35, 'R&amp;D', PL), (20, 'Prototypes &amp; tooling', '#5B4785'), (15, 'User &amp; institution pilots', GD), (10, 'Regulatory, testing, IP', '#C98A3A'), (10, 'Key hires', '#8F84A8'), (10, 'Reserve', '#C9C1B4')]
bar = '<div style="display: flex; height: 16px; margin-top: 8px">' + ''.join(f'<div style="width: {w}%; background: {c}"></div>' for w, _, c in alloc) + '</div>'
leg = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2px 12px; padding-top: 6px">' + ''.join(f'<div class="b" style="font-size: 11px; color: #333; display: flex; gap: 6px; align-items: center"><span style="width: 9px; height: 9px; background: {c}; flex: none"></span>{w}% {t}</div>' for w, t, c in alloc) + '</div>'
partners = [('Pilot partners', 'hearing centres, fitting clinics, ENT and rehab institutions, elderly-care communities'), ('Manufacturing', 'ODM/OEM makers with hearing-aid, earbud and medical-electronics experience; rehab-equipment makers for the mattress'), ('Advisers', 'audiologists, clinical advisers and older users inside the design loop')]
pt = ''.join(f'<div class="sr" style="font-size: 12px; line-height: 1.38; color: #333; padding-top: 4px"><b style="color: {PL}">{a}:</b> {b}</div>' for a, b in partners)
fund = colhead(1436, 428, 'Funding &amp; partners') + f'<div class="sr" style="font-size: 12.5px; line-height: 1.4; color: #333; padding-top: 7px">First external round planned at <b>¥5–8 M</b> for about 18 months, spent on engineering, not advertising:</div>{bar}{leg}<div style="border-top: 1px solid #D9D2C3; margin-top: 8px; padding-top: 2px">{pt}</div></div>'

top = f"""<div class="m" style="position: absolute; left: 56px; top: 34px; right: 56px; display: flex; justify-content: space-between; font-size: 11px; color: {PL}; border-bottom: 2px solid {INK}; padding-bottom: 6px"><span>05 — Mind · Research Nº 04 · the company</span><span>Amy Hu · 20</span></div>
<div style="position: absolute; left: 56px; top: 74px; width: 640px; display: flex; flex-direction: column; gap: 10px; color: {INK}">
<div class="pf" style="font-size: 35px; line-height: 1.05; font-weight: 900; white-space: nowrap">Beijing Lingtong <span style="color: {PL}; font-style: italic">Future Technology</span></div>
<div class="sr" style="font-size: 15px; line-height: 1.42; font-style: italic; color: #444"><b style="font-style: normal; color: {INK}">Mission.</b> A human-centred assistive technology company: turning research on hearing and patient care into products people can buy, use and trust.</div>
<div class="m" style="font-size: 10.5px; color: #555">Founded by Amy Hu · a team of about five · USD 100k+ raised</div>
</div>
<div class="abs" style="position: absolute; left: 740px; top: 78px; width: 760px; column-count: 2; column-gap: 28px; color: {INK}; border-top: 1px solid {INK}; padding-top: 8px; font-size: 13px"><b style="color: {PL}">Motivations</b> &nbsp;A paper proves an idea works; only a product reaches the person who needs it. Both of my engineering projects began with someone I know: my grandfather, who struggled to hear, and my own weeks on an injured leg. Research at Peking University and the Conrad Challenge gave us working prototypes, so I founded Beijing Lingtong Future Technology to carry them further. The company keeps one small R&amp;D team behind both products, so what we learn about sensors, control and testing on one is reused on the other. Each co-founder owns one side of the business, and every spending decision is checked against our five-year model. As founder and CTO, I lead the technology for both products and pitch them to investors and hospitals.</div>
<img src="/_blob/78f7f49b8d10aecff86c08796220092f" alt="Lingtong logo" style="position: absolute; left: 1600px; top: 70px; height: 172px; display: block">
"""
body = top + band + prods + model + roadmap + fund + kws([('$100k+', 'raised so far'), ('~5', 'people on the team'), ('¥5–8 M', 'first external round planned'), ('1.5 bn', 'people with hearing loss (WHO)'), ('323 M', 'Chinese aged 60+, end of 2025'), ('&lt;5%', 'hearing-aid penetration in China')], 56, 1808, 20)
write('Mind-Startup.dc.html', 'Lingtong startup', PAPER, body)
