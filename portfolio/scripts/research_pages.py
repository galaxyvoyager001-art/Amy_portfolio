"""Research & Entrepreneurship detail pages (docs/work/). Two chapters with one shared structure:
Asking   (I The question · II The method · III The finding · IV Beyond)
Building (I For whom · II The problem · III What we built · IV Where it stands)"""
import os, re, glob, html
from PIL import Image

ROOT = '/home/user/Amy_portfolio'
A = ROOT + '/portfolio/assets/'
OUT = ROOT + '/docs/work/'
IMG = ROOT + '/docs/site/img/w/'
src = open(os.path.join(os.path.dirname(__file__), 'build_work.py')).read()
NAV = re.search(r"NAV = '''(.*?)'''", src, re.S).group(1)

ID2NAME = {}
for l in open(A + 'blob-map.txt'):
    p = l.split()
    if len(p) == 2: ID2NAME[p[1]] = p[0]

def img(ref, w=1500):
    name = ref
    if not glob.glob(A + ref + '.*'):
        hits = [n for i, n in ID2NAME.items() if i.startswith(ref)]
        if hits: name = hits[0]
    f = (glob.glob(A + name + '.*') or [None])[0]
    if not f: raise SystemExit(f'missing image {ref}')
    out = IMG + name + '.webp'
    if not os.path.exists(out):
        im = Image.open(f)
        if im.mode not in ('RGB', 'RGBA'): im = im.convert('RGBA')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        im.save(out, 'WEBP', quality=84)
    return '../site/img/w/' + name + '.webp'

# ---------------------------------------------------------------- building blocks
class Page:
    def __init__(self): self.n = 0
    def F(self, ref, cap, kind='', ar=None):
        self.n += 1
        st = f' style="aspect-ratio:{ar}"' if ar else ''
        return (f'<figure class="rf {kind}"><div class="rf-fr"{st}><img src="{img(ref)}" alt="{html.escape(re.sub("<[^>]+>", "", cap))}" loading="lazy"></div>'
                f'<figcaption><b class="m">Fig. {self.n}</b><span>{cap}</span></figcaption></figure>')

def P(*ps): return ''.join(f'<p>{p}</p>' for p in ps)
def ROW(a, b, rev=False): return f'<div class="r-row{" rev" if rev else ""}"><div class="r-txt">{a}</div><div>{b}</div></div>'
def GRID(cols, *figs): return f'<div class="r-grid" style="--c:{cols}">{"".join(figs)}</div>'
def LAB(title, inner, note=''): return f'<div class="trylab"><div class="trylab-h m"><span>Try it</span><span>{title}</span></div>{inner}{f"<p class=trylab-note>{note}</p>" if note else ""}</div>'
def NUMS(*items): return '<div class="r-nums">' + ''.join(f'<div><b class="d">{a}</b><span>{b}</span></div>' for a, b in items) + '</div>'
def LIST(*rows): return '<div class="r-list">' + ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in rows) + '</div>'
def PULL(t): return f'<blockquote class="r-pull">{t}</blockquote>'

ASK = ['The question', 'The method', 'The finding', 'Beyond']
BUILD = ['For whom', 'The problem', 'What we built', 'Where it stands']
ROMAN = ['I', 'II', 'III', 'IV']

def page(d, nxt):
    heads = ASK if d['ch'] == 'ask' else BUILD
    chap = 'Chapter I · Asking' if d['ch'] == 'ask' else 'Chapter II · Building'
    toc = ''.join(f'<a href="#s{i + 1}"><span class="m">{ROMAN[i]}</span>{h}</a>' for i, h in enumerate(heads))
    secs = ''.join(f'<section class="r-sec" id="s{i + 1}"><header class="r-sh"><span class="r-rn">{ROMAN[i]}</span><h2 class="d">{heads[i]}</h2></header><div class="r-body">{b}</div></section>'
                   for i, b in enumerate(d['secs']))
    meta = ''.join(f'<div><span class="m">{a}</span><span>{b}</span></div>' for a, b in d['meta'])
    hero_cls = 'r-heroimg ' + d.get('hero_kind', 'cut')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d["name"]} — Amy Hu</title>
<meta name="description" content="{html.escape(d["desc"])}">
<meta property="og:image" content="{img(d["hero"])}">
<link rel="stylesheet" href="../site/style.css">
<link rel="stylesheet" href="../site/work.css">
<link rel="stylesheet" href="../site/research.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22%3E%3Ccircle cx=%2216%22 cy=%2216%22 r=%2214%22 fill=%22%23FF5A1F%22/%3E%3C/svg%3E">
</head>
<body class="work rs rs-{d["ch"]}" style="--a:{d["a"]}">
{NAV}
<main>
<header class="r-hero">
  <div class="r-kick m"><span>{chap} · {d["no"]}</span><span>{d["where"]}</span></div>
  <div class="r-name d">{d["name"]}</div>
  <h1 class="r-q">{d["q"]}</h1>
  <div class="{hero_cls}"><img src="{img(d["hero"])}" alt="{html.escape(d["hero_alt"])}"></div>
  <div class="r-meta">{meta}</div>
</header>
<div class="r-wrap">
  <nav class="r-toc" aria-label="Sections">{toc}</nav>
  <div class="r-main">{secs}</div>
</div>
</main>
<a class="nextp" href="{nxt["slug"]}.html" data-cursor="Next"><span class="m">{nxt["label"]} →</span><div class="d t">{nxt["name"]}</div><img src="{img(nxt["hero"])}" alt=""></a>
<footer class="footer" style="padding-top:8vh"><div class="legal m" style="margin-top:0"><span>© 2026 Amy Hu</span><a href="../index.html#research">All research</a><a href="../portfolio/index.html">Full portfolio</a></div></footer>
<script src="../site/vendor/gsap.min.js"></script>
<script src="../site/vendor/ScrollTrigger.min.js"></script>
<script src="../site/vendor/lenis.min.js"></script>
<script src="../site/work.js"></script>
<script src="../site/research.js"></script>
</body>
</html>
'''

PAGES = []

# ================================================================ ASKING 01 · PENDULUMS
g = Page()
PAGES.append(dict(slug='physics-tournaments', ch='ask', no='01 / 04', name='Coupled Pendulums', a='#2B48D6',
  q='How does energy travel through a chain of magnets?', where='IB Extended Essay · IYPT · CYPT 2026',
  hero='cut_ee_rig', hero_alt='My 3D-printed magnetic pendulum rig', desc='A chain of magnetically coupled pendulums: normal modes, energy transport and localization.',
  meta=[('Role', 'Researcher · team captain'), ('Model', 'Lagrangian, 2–5 pendulums'), ('Agreement', '1.37% mean difference'), ('Also', 'Founder of Wavefront, our school physics lab')],
  secs=[
    ROW(P('Hang pendulums side by side with magnets at their tips and they stop being independent. Push one and its energy leaks into its neighbours, then returns, then wanders off again. A chain like this is a desktop picture of atoms in a crystal trading energy.',
          '<b>My question:</b> how do magnet strength, spacing, length and release angle shift the chain’s normal-mode frequencies, and how does that decide whether energy spreads through the chain, comes back, or stays trapped in one place?'),
        g.F('ee_model', 'The idealised chain: rigid pendulums, magnets at the tips, repelling neighbours', 'contain')),
    ROW(P('I designed and 3D-printed the apparatus: a rigid top rail, sliding PETG brackets that set the spacing, bearing-mounted arms and magnets held in baskets.',
          'Every trial was filmed at 30 frames per second and tracked in Tracker. A Fourier transform of each trace gives the eigenfrequencies, which I compared with a Lagrangian model of the chain.'),
        g.F('ee_rig', 'My rig: brackets set the spacing; bearings and baskets hold the magnets'), rev=True)
    + NUMS(('100+', 'filmed trials'), ('30 fps', 'video, tracked frame by frame'), ('2–5', 'pendulums per chain')),
    P('The model and the rig agree: across all trials the measured normal-mode frequencies differ from the predictions by 1.37% on average. The nearly in-phase mode is set by gravity alone, while the higher modes rise with magnetic moment and fall steeply with spacing. Larger release angles soften every frequency.')
    + LAB('A chain of five', '<div class="pend" data-lab="pendulums"><canvas></canvas><div class="pend-ui"><label class="m">Coupling <input type="range" min="0.2" max="3" step="0.05" value="1.2"></label><button class="m" type="button" data-kick>Kick pendulum 1</button></div><div class="pend-e"></div></div>',
          'A simplified linear model, not my full Lagrangian. Click a pendulum to push it, and watch its energy (bars below) travel down the chain and come back. Stronger coupling, as with closer magnets, moves energy faster.')
    + GRID(3, g.F('ee_modes_t', 'Normal modes of a five-pendulum chain', 'contain'), g.F('ee_fft_t', 'Theory against experiment, in time and frequency', 'contain'), g.F('ee_energy_t', 'Energy spreading, recurrence and self-localization', 'contain')),
    P('At CYPT 2026 I reported two more problems with the same method: model first, then a rig I built and bought the parts for myself.')
    + ROW(P('<b>Electrical damping.</b> A magnet on a spring oscillates inside a coil wired to a resistor. I predicted that damping peaks near 2,700 turns, falls as 1/R and grows with the square of the magnetic moment. My data followed all three trends.'), g.F('cy_ed_rig_cut', 'My electrical damping rig', 'cut'))
    + ROW(P('<b>Levitation control.</b> Pyrolytic graphite floats over a checkerboard of magnets; a laser heats one edge so the force becomes uneven and the sheet should slide. My N52 magnets held the sheet too firmly for a 1.6 W beam, and the model shows what to change next.'), g.F('cy_ph_laser', 'The laser on a 2-D gantry over the magnet array'), rev=True)
    + P('As captain I took each problem apart with the team into physics, model and experiment, and we rehearsed the opposition and review rounds together.')
    + GRID(3, g.F('cy_ph_discuss', 'Leading a team discussion'), g.F('cy_ph_present', 'Reporting at CYPT 2026'), g.F('cy_ph_team', 'The team at work')),
  ]))

# ================================================================ ASKING 02 · METALLIC GLASS
g = Page()
PAGES.append(dict(slug='metallic-glass', ch='ask', no='02 / 04', name='Flowed Metal', a='#C4521F',
  q='What does heat do to a metal that is also a glass?', where='Chinese Academy of Sciences, Institute of Mechanics',
  hero='lab_setup', hero_kind='photo', hero_alt='The laser-induced particle impact platform', desc='Micro-particle impacts on a Pd-based metallic glass at 25, 100 and 200 °C.',
  meta=[('Role', 'First author'), ('Supervisor', 'Prof. Minqiang Jiang'), ('Recognition', 'ISEF Beijing qualifier'), ('Material', 'Pd-based metallic glass')],
  secs=[
    P('Glass shatters; metal bends. A metallic glass is a metal whose atoms are frozen in disorder, like a glass, so it is unusually strong. But heat it toward its glass transition and it may start to flow.',
      '<b>My question:</b> when a tiny particle hits it at hundreds of metres per second, does heat make a metallic glass harder, like a metal, or softer, like a glass?'),
    ROW(P('A 7 ns, 532 nm laser pulse ablates a gold film and launches a 30 µm silica particle at 1–1000 m/s. A camera at up to five million frames per second records the impact and rebound, and a PID controller holds the target within ±1 K at 25, 100 or 200 °C.',
          'I prepared and characterised every sample, ran every impact, and measured the craters by SEM and confocal microscopy.'),
        g.F('fm_hs25', 'High-speed frames: the particle falls in and rebounds', 'contain'))
    + NUMS(('5 M', 'frames per second'), ('±1 K', 'temperature control'), ('100+', 'impact tests')),
    P('Softer, and more like a fluid. From 25 to 200 °C the glass absorbs more of the impact energy, its dynamic yield strength falls by 10.4%, and the crater rim no longer stays neat: it splashes outward like a viscous liquid.')
    + LAB('Drag to compare the craters', f'<div class="cmp" data-lab="compare"><img src="{img("bmg_sem200")}" alt="Crater at 200 °C"><div class="cmp-top"><img src="{img("bmg_sem25")}" alt="Crater at 25 °C"></div><div class="cmp-bar"><span class="m">25 °C</span><i></i><span class="m">200 °C</span></div></div>',
          'Left of the line: a crater at 25 °C, with a regular rim. Right: at 200 °C, a splash-like pile-up.')
    + GRID(2, g.F('fm_y25', 'Dynamic yield strength at 25 °C', 'contain'), g.F('fm_y200', 'Dynamic yield strength at 200 °C', 'contain')),
    ROW(P('Why does it happen? I built a quarter-symmetric ABAQUS model with 1.35 million elements and a coupled shear-transformation / free-volume law. It reproduced the measured crater and showed the mechanism: at 200 °C the contact lasts longer, stress is lower, and many more shear transformation zones switch on.'),
        g.F('fm_sim', 'Field-averaged stress, plastic strain and shear-transformation density', 'contain'))
    + GRID(2, g.F('bmg_cor', 'Coefficient of restitution against impact speed', 'contain'), g.F('fm_xrd', 'X-ray diffraction confirms the sample is amorphous', 'contain')),
  ]))

# ================================================================ ASKING 03 · OPTICS
g = Page()
PAGES.append(dict(slug='optics', ch='ask', no='03 / 04', name='Light, Measured', a='#2F7D4F',
  q='How precisely can light be measured and controlled?', where='Peking University, Institute of Physics',
  hero='op_ph4', hero_kind='photo', hero_alt='Laser and spectrometer bench', desc='Twelve experimental optics reports, polarisation control, and Raman and laser systems.',
  meta=[('Role', 'Nonlinear optics research intern'), ('Reports', '12, each written in full'), ('Systems', 'Raman, lasers, polarisation'), ('States tested', '20+ polarisation states')],
  secs=[
    P('Every number in an optics textbook was once measured by someone at a bench. These experiments asked how close I could get to those numbers with my own hands.',
      '<b>My question:</b> how precisely can light be measured, and how deliberately can its polarisation be controlled?'),
    P('I worked through twelve classic experiments, built every set-up myself and wrote each one up as a full report with an error analysis. The habits that mattered most: read many fringes at once, measure both sides of a pattern, and turn every screw in one direction only.')
    + GRID(4, g.F('op_ph3', 'An optical table I aligned', ar='3/4'), g.F('lab_comp', 'At the bench', ar='3/4'), g.F('op_ph1', 'My labelled sample', ar='3/4'), g.F('op_ph2', 'The clean-room entrance', ar='3/4')),
    P('The measurements land close to the reference values: a He-Ne wavelength of about 633 nm against 632.8 nm, and Malus’s law within 0.4% at 45°.')
    + LAB('Malus’s law', '<div class="malus" data-lab="malus"><svg viewBox="0 0 640 300"></svg><label class="m">Analyser angle <input type="range" min="0" max="180" step="1" value="45"><output>45°</output></label></div>',
          'Light through two polarisers has intensity I = I₀ cos²θ. The dot marks my measurement at 45°: I/I₀ = 0.502, against 0.500 in theory.')
    + LIST(('Thin lens', 'f = 100.0 mm by the conjugate method'), ('Newton’s rings', 'Lens radius ≈ 0.85 m'), ('Air wedge', 'Sheet thickness ≈ 74 µm'), ('Young’s double slit', 'He-Ne wavelength ≈ 633 nm'), ('Diffraction grating', 'Mercury green line ≈ 546 nm'), ('Malus’s law', 'I/I₀ = 0.502 at 45°'), ('Abbe refractometer', 'Water 1.3330, sugar solution 1.3474'), ('Holography', 'A 3-D image rebuilt from a plate')),
    ROW(P('As a research intern in a nonlinear optics group at Peking University’s Institute of Physics, I also operated Raman and laser systems normally used by graduate students and tested more than twenty polarisation states of the beam.'),
        g.F('lab_amy', 'In the lab', ar='4/5')),
  ]))

# ================================================================ ASKING 04 · MODELLING
g = Page()
papers = [('IMMC 2024', 'Saving the Panama Canal’s water', 'From the water exchange between lock chambers and water-saving basins, the optimal number and size of basins, then one cost model for energy, maintenance, water, labour and materials.', '70058dcf'),
          ('IMMC 2025', 'Teaching a robot to jump rope', 'The spinning rope as a catenary using the Jacobi elliptic function sn, drawn at every moment in MATLAB, to find the jump speeds, times and rope lengths that work.', 'ff4b7949'),
          ('HiMCM 2025 · Finalist', 'Sweeping a burning building', 'A cellular automaton for fire, smoke and occupants; mixed-integer programming for the fastest route and the number of responders.', '226909ee'),
          ('IMMC 2026', 'Is Friday the 13th unlucky?', 'A Boltzmann-style expectation model and information theory over 25 years of disasters. Friday the 13th scored 5.56 against a maximum of 18.21.', 'f0746e71'),
          ('IMMC 2026', 'Guarding Etosha', 'Risk mapping, topological decomposition, Snake-algorithm patrol loops and a Kalman-filter revisit interval for rangers.', 'c23a2b81')]
cards = ''.join(f'<article class="pcard"><div class="pc-img"><img src="{img(r)}" alt="{t}" loading="lazy"></div><span class="m">{c}</span><h3 class="d">{t}</h3><p>{d}</p></article>' for c, t, d, r in papers)
PAGES.append(dict(slug='modelling', ch='ask', no='04 / 04', name='Modelling the World', a='#C8641E',
  q='How do you turn a messy problem into a model you can test?', where='IMMC · HiMCM',
  hero='mm_cover', hero_kind='photo', hero_alt='Applied Mathematics, Vol. 2', desc='Five mathematical modelling papers for IMMC and HiMCM, and an applied mathematics journal.',
  meta=[('Role', 'Team captain · main modeller'), ('Papers', 'Five, all written by me'), ('Awards', '3 Finalist awards'), ('Also', 'Editor, school mathematics journal')],
  secs=[
    P('A modelling contest hands you a messy real situation and a few days. There is no right answer at the back of the book, only better and worse simplifications.',
      '<b>My question,</b> asked five times: which variables matter, which assumptions can I defend, and how do I know the model is telling the truth?'),
    P('The same four steps each time. As captain I split the problem into sub-models, built the core model myself and wrote the paper against the deadline.')
    + '<ol class="r-steps"><li><b>Simplify</b><span>Name the variables; state every assumption.</span></li><li><b>Model</b><span>Choose the mathematics that fits the mechanism.</span></li><li><b>Test</b><span>Check against data, limits and sensitivity.</span></li><li><b>Explain</b><span>Write it so a non-specialist can act on it.</span></li></ol>',
    P('Five problems, five different kinds of mathematics. Scroll sideways through the papers.')
    + f'<div class="pcards" data-lab="drag">{cards}</div>'
    + NUMS(('5', 'papers, all written by me'), ('3×', 'Finalist awards'), ('Vol. 2', 'journal issue on IMMC')),
    ROW(P('I also edit our school’s applied mathematics journal. Volume 2 is devoted to IMMC.'),
        g.F('mm_cover', 'Applied Mathematics, Vol. 2', ar='3/4')),
  ]))

# ================================================================ BUILDING 05 · SMARTHEARING
g = Page()
scenes = [('Street', 'Car horn', ['Traffic', 'Wind', 'Footsteps', 'Car horn']), ('Restaurant', 'Speech', ['Dishes', 'Music', 'Chatter', 'Speech']), ('Home', 'Crying infant', ['Television', 'Kettle', 'Fan', 'Crying infant'])]
sbtn = ''.join(f'<button class="m{" on" if i == 0 else ""}" type="button" data-i="{i}">{s}</button>' for i, (s, *_ ) in enumerate(scenes))
sset = ''.join(f'<div class="sc-set{" on" if i == 0 else ""}" data-i="{i}">' + ''.join(f'<span class="chip{" key" if x == k else ""}">{x}</span>' for x in xs) + '</div>' for i, (s, k, xs) in enumerate(scenes))
PAGES.append(dict(slug='smarthearing', ch='build', no='05 / 07', name='SmartHearing', a='#E2553F',
  q='For people who hear less than they used to, like my grandfather.', where='Peking University, Institute for AI',
  hero='lt_hearing', hero_kind='photo', hero_alt='SmartHearing hearing-aid prototype', desc='A scene-adaptive hearing aid that uses an audio language model to decide which sound matters.',
  meta=[('Role', 'Product design lead · equal-contribution author'), ('Output', 'Patent · ICASSP 2027 submission'), ('Test', '101 listeners'), ('Company', 'Now Lingtong’s main product')],
  secs=[
    P('My grandfather’s hearing has been fading for years. Watching him miss things taught me to notice the quiet details of everyday life, and to worry about the loud ones he might not hear at all.',
      'SmartHearing is for him, and for anyone whose hearing aid makes the world louder without making it clearer.'),
    P('A conventional hearing aid amplifies speech. But which sound matters most depends on where you are: a car horn in the street, a voice in a restaurant, a crying infant at home. Amplify the wrong one and the important sound is buried.')
    + LAB('Which sound matters here?', f'<div class="scn" data-lab="scenes"><div class="scn-b">{sbtn}</div><div class="scn-s">{sset}</div></div>',
          'The same device must bring forward a different sound in each place. SmartHearing listens to the scene first, then decides.'),
    ROW(P('<b>Perceive, decide, act.</b> A large audio language model describes each sound in the scene: what it is, how dangerous, how relevant. A Query-space Adapter translates those descriptions into the language a sound separator understands, and the separator extracts each source so the device can raise warnings, keep useful ambience and suppress noise.'),
        g.F('sh_arch_t', 'System architecture: perception path, Adapter, execution path', 'contain'))
    + GRID(1, g.F('sh_scenes', 'The target sound depends on the scene', ar='4/3')).replace('class="r-grid"', 'class="r-grid narrow"'),
    P('On 145 unseen mixtures the gains held, and in a 101-person listening test SmartHearing was rated most salient in 50.5% of trials, against 28.1% and 21.5% for the baselines. The work is patented and submitted to ICASSP 2027, and it is now the main product of Lingtong, the company I founded.')
    + NUMS(('50.5%', 'trials rated most salient'), ('101', 'listening-test participants'), ('+1.14 dB', 'SI-SDRi gain from our Adapter'), ('1', 'patent')),
  ]))

# ================================================================ BUILDING 06 · CURAWAVE
g = Page()
units = ''.join('<i></i>' for _ in range(12))
PAGES.append(dict(slug='curawave', ch='build', no='06 / 07', name='Curawave', a='#24B3A6',
  q='For patients who must be moved between beds after surgery.', where='Conrad Challenge',
  hero='mattress_v2', hero_alt='Curawave mattress concept rendering', desc='A wave-bionic soft robotic mattress that slides a patient sideways onto another bed.',
  meta=[('Role', 'CTO'), ('Built', 'Moulds, silicone units, valves, Arduino'), ('Prototypes', '3 generations'), ('Company', 'Lingtong’s second product')],
  secs=[
    P('After surgery, a patient who cannot move must still be moved: from trolley to bed, from bed to scanner. Today that means several people lifting at once.',
      'I spent weeks on an injured leg and learned how helpless it feels to be shifted by other people’s hands. Curawave is for patients in that position, and for the nurses who lift them.'),
    P('Every transfer is a risk. Among 1,200 post-operative patients in one study, 15% had complications related to being moved. Lifting also injures the people who do it.')
    + NUMS(('15%', 'of 1,200 patients had transfer-related complications, in one study'), ('0', 'people lifting, with Curawave')),
    P('Curawave moves a patient the way a wave moves a boat. The mattress is made of soft units that tilt left and right in alternating groups, so a sideways wave carries the patient onto the next bed.')
    + LAB('A row of units', f'<div class="wave" data-lab="wave"><div class="wv-p"></div><div class="wv-u">{units}</div></div>',
          'Alternating groups inflate and tilt in turn; the patient (the bar) is passed along the top.')
    + ROW(P('Each unit has a hollow silicone inflation layer, a non-stretch cotton confining layer and a silicone base. Because the confining layer stretches less, the unit tilts sideways when inflated.'), g.F('cw_principle', 'How one unit tilts and pushes', 'contain'))
    + GRID(3, g.F('cw_units', 'Cast silicone units'), g.F('cw_circuit', 'Pump, valves and Arduino wiring'), g.F('cw_unit_cad', 'A unit modelled in Fusion', 'contain')),
    P('We built three prototype generations, up to a 1 × 4 array with each group on its own solenoid valve and an Arduino timing the wave. The full design is 18 × 20 units. Curawave was our Conrad Challenge entry and now continues inside Lingtong as our second product line.')
    + GRID(2, g.F('cw_concept', 'The full mattress concept', 'contain'), g.F('cw_slide10', '18 × 20 units, grouped to act in turn', 'contain')),
  ]))

# ================================================================ BUILDING 07 · LINGTONG
g = Page()
PAGES.append(dict(slug='lingtong', ch='build', no='07 / 07', name='Lingtong', a='#E0A93B',
  q='For both: a company to carry two prototypes to the people who need them.', where='Lingtong Future Technology · Beijing',
  hero='lt_logo', hero_kind='logo', hero_alt='Lingtong logo', desc='Lingtong Future Technology: an assistive technology startup built around SmartHearing and Curawave.',
  meta=[('Role', 'Founder &amp; CTO'), ('Team', 'About five people'), ('Raised', 'USD 100k+'), ('Trademarks', 'Two, filed 2026')],
  secs=[
    P('A paper proves an idea works; only a product reaches the person who needs it. Lingtong exists for the users of both projects: people losing their hearing, and patients who must be moved.')
    + '<div class="merge"><span>SmartHearing</span><i>+</i><span>Curawave</span><i>→</i><b class="d">Lingtong</b></div>',
    P('Research ends with a prototype on a lab bench. Between that and a device in someone’s home there is design, certification, manufacturing, sales and service, and none of it happens without a company.'),
    P('For the first 18 months, 70–80% of our resources go to SmartHearing; Curawave continues as the second growth curve.')
    + LIST(('SmartHearing', 'AI hearing system that decides which sound you need to hear. Patent filed.'), ('Curawave', 'Wave-bionic transfer mattress for hospitals and care homes. Three prototype generations.'))
    + P('Three ways to earn: own-brand devices with long-term service (basic hearing never behind a subscription), institutional solutions for hearing centres, care homes and hospitals, and licensing an Auditory Decision Engine SDK to makers of earbuds, hearing aids and smart glasses.'),
    NUMS(('$100k+', 'raised so far'), ('2', 'trademark applications'), ('5', 'people on the team'))
    + '<ol class="tl" data-lab="timeline"><li><span class="m">0–6 months</span><b>Wearable prototype</b><em>From research prototype to wearable SmartHearing; device-classification advice.</em></li><li><span class="m">6–12 months</span><b>Pilots</b><em>100–300 users and 3–5 partner institutions.</em></li><li><span class="m">12–24 months</span><b>First sales</b><em>Design freeze, registration path, first paid sales.</em></li><li><span class="m">24–36 months</span><b>Scale</b><em>National channels; licensing begins.</em></li></ol>'
    + P('Trademark application No. 92712127 (Class 42) was accepted on 20 July 2026; No. 92712148 passed preliminary examination and was published on 27 September 2026.')
    + GRID(2, g.F('lt_tm1', 'Acceptance notice, CNIPA', 'contain', '3/4'), g.F('lt_tm2', 'Preliminary approval notice, CNIPA', 'contain', '3/4')).replace('class="r-grid"', 'class="r-grid narrow"'),
  ]))

# ---------------------------------------------------------------- write, chained in order; the last returns to the start of the site
CHAIN = {p['slug']: p for p in PAGES}
for i, p in enumerate(PAGES):
    if i + 1 < len(PAGES):
        n = PAGES[i + 1]
        lab = 'Next · Chapter II · Building' if n['ch'] != p['ch'] else ('Next · ' + ('Asking' if n['ch'] == 'ask' else 'Building') + ' ' + n['no'].split(' ')[0])
        nxt = dict(slug=n['slug'], name=n['name'], hero=n['hero'], label=lab)
    else:
        nxt = dict(slug='tactile-books', name='Even without sight', hero='cut_book_closed', label='Back to the senses · Touch')
    open(OUT + p['slug'] + '.html', 'w').write(page(p, nxt))
    print('wrote', p['slug'])
