"""Generate project detail pages for the personal website (docs/website/work/*.html)."""
import glob, os, html
from PIL import Image

ROOT = '/home/user/Amy_portfolio'
A = ROOT + '/portfolio/assets/'
OUT = ROOT + '/docs/website/work/'
IMG = ROOT + '/docs/website/site/img/w/'
os.makedirs(OUT, exist_ok=True); os.makedirs(IMG, exist_ok=True)

ID2NAME = {}
for l in open(A + 'blob-map.txt'):
    p = l.split()
    if len(p) == 2: ID2NAME[p[1]] = p[0]

def img(ref, w=1500):
    """ref: asset name or blob-id prefix -> web path of a resized copy."""
    name = ref
    if ref not in [os.path.splitext(os.path.basename(f))[0] for f in glob.glob(A + ref + '.*')]:
        hits = [n for i, n in ID2NAME.items() if i.startswith(ref)]
        if hits: name = hits[0]
    src = (glob.glob(A + name + '.*') or [None])[0]
    if not src: raise SystemExit(f'missing image {ref}')
    out = IMG + name + '.webp'
    if not os.path.exists(out):
        im = Image.open(src)
        if im.mode not in ('RGB', 'RGBA'): im = im.convert('RGBA')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        im.save(out, 'WEBP', quality=82)
    return '../site/img/w/' + name + '.webp'

def fig(ref, cap='', tag='', kind='', ar=None):
    style = f' style="aspect-ratio:{ar}"' if ar else ''
    return (f'<figure class="fig {kind}"><div class="fr"{style}><img src="{img(ref)}" alt="{html.escape(cap)}" loading="lazy"></div>'
            + (f'<figcaption><span>{cap}</span><span class="m">{tag}</span></figcaption>' if cap or tag else '') + '</figure>')

def blocks(bs):
    out = ''
    for b in bs:
        k = b[0]
        if k == 'two':
            _, n, t, ps, f, rev = b
            out += f'<section class="blk"><div class="two{" rev" if rev else ""}"><div class="txt"><h2 class="d"><span class="n">{n}</span>{t}</h2>{"".join(f"<p>{p}</p>" for p in ps)}</div>{f}</div></section>'
        elif k == 'full':
            out += f'<section class="full">{b[1]}</section>'
        elif k == 'grid':
            _, n, t, intro, cols, ar, figs = b
            head = f'<h2 class="d"><span class="n">{n}</span>{t}</h2>' if t else ''
            out += f'<section class="blk">{head}{"<p class=lead>" + intro + "</p>" if intro else ""}<div class="gridf" style="--c:{cols};--ar:{ar}">{"".join(figs)}</div></section>'
        elif k == 'steps':
            _, n, t, intro, items, band = b
            st = ''.join(f'<div class="step"><span class="d">{i + 1:02d}</span><b>{a}</b><span>{d}</span></div>' for i, (a, d) in enumerate(items))
            inner = f'<h2 class="d"><span class="n">{n}</span>{t}</h2>{"<p class=lead>" + intro + "</p>" if intro else ""}<div class="steps" style="--c:{min(len(items), 4)}">{st}</div>'
            out += f'<section class="band">{inner}</section>' if band else f'<section class="blk">{inner}</section>'
        elif k == 'quote':
            out += f'<section class="quote"><blockquote>{b[1]}<cite class="m">{b[2]}</cite></blockquote></section>'
        elif k == 'list':
            _, n, t, intro, rows = b
            out += f'<section class="blk"><div class="two"><div class="txt"><h2 class="d"><span class="n">{n}</span>{t}</h2>{"<p>" + intro + "</p>" if intro else ""}</div><div class="list">{"".join(f"<div><b>{a}</b><span>{c}</span></div>" for a, c in rows)}</div></div></section>'
        elif k == 'notes':
            _, n, t, intro, notes = b
            out += f'<section class="blk"><h2 class="d"><span class="n">{n}</span>{t}</h2>{"<p class=lead>" + intro + "</p>" if intro else ""}<div class="notes">{"".join(f"<div class=note>{a}<span>{w}</span></div>" for a, w in notes)}</div></section>'
        elif k == 'text':
            _, n, t, ps = b
            out += f'<section class="blk"><h2 class="d"><span class="n">{n}</span>{t}</h2>{"".join(f"<p>{p}</p>" for p in ps)}</section>'
    return out

NAV = '''<div class="curtain" aria-hidden="true" style="transform:translateY(0)"></div>
<div class="cursor" aria-hidden="true"><div class="ring"><span>View</span></div><div class="dot"></div></div>
<nav class="nav"><a href="../index.html#made" class="m back">← All work</a><a href="../index.html" class="d brand">Amy <b>Hu</b></a><div class="nav-r"><a class="navpf m" href="../../">Portfolio ↗</a><button class="navbtn m" aria-expanded="false" aria-controls="menu"><span class="lab">Menu</span><span class="lines"><i></i><i></i></span></button></div></nav>
<div class="menu" id="menu">
  <div class="imgs"><img data-k="home" src="../site/img/hero.webp" alt="" class="on"><img data-k="made" src="../site/img/visit.webp" alt=""><img data-k="research" src="../site/img/lab.webp" alt=""><img data-k="gallery" src="../site/img/guzhengduo.webp" alt=""><img data-k="portfolio" src="../site/img/stage.webp" alt=""></div>
  <ul>
    <li><a class="d" href="../index.html" data-k="home"><small>01</small>Home</a></li>
    <li><a class="d" href="../index.html#made" data-k="made"><small>02</small>Senses</a></li>
    <li><a class="d" href="../index.html#research" data-k="research"><small>03</small>Research</a></li>
    <li><a class="d" href="../index.html#gallery" data-k="gallery"><small>04</small>Gallery</a></li>
    <li><a class="d" href="../../" data-k="portfolio"><small>05</small>Portfolio</a></li>
  </ul>
  <div class="foot m"><span>Touch · Sight · Taste · Sound · Mind</span><span>Beijing</span></div>
</div>'''

def page(p, nxt):
    title_lines = ''.join(f'<span class="ln"><span>{l}</span></span>' for l in p['title'])
    meta = ''.join(f'<div><span class="m">{a}</span><span>{b}</span></div>' for a, b in p['meta'])
    facts = ''.join(f'<div class="stat"><b class="d" data-count="{c}" data-prefix="{pre}" data-suffix="{suf}" data-dec="{dec}">{pre}0{suf}</b><span>{t}</span></div>' for c, pre, suf, dec, t in p['facts'])
    hk = ('heroimg photo' if p.get('hero_photo') else 'heroimg') + (' small' if p.get('hero_small') else '')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["seo"]} — Amy Hu</title>
<meta name="description" content="{html.escape(p["intro_plain"])}">
<meta property="og:image" content="{img(p["hero"])}">
<link rel="stylesheet" href="../site/style.css">
<link rel="stylesheet" href="../site/work.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22%3E%3Ccircle cx=%2216%22 cy=%2216%22 r=%2214%22 fill=%22%23FF5A1F%22/%3E%3C/svg%3E">
</head>
<body class="work" style="--pc:{p["c"]};--pt:{p["t"]};--pa:{p["a"]};--pa2:{p["a2"]}">
{NAV}
<main>
<header class="w-hero">
  <div class="{hk}"><img src="{img(p["hero"])}" alt="{html.escape(p["hero_alt"])}"></div>
  <span class="m kick">{p["kicker"]}</span>
  <h1 class="d">{title_lines}</h1>
  <div class="sub">{p["sub"]}</div>
  <div class="w-meta">{meta}</div>
</header>
<section class="w-intro"><span class="m">( Overview )</span><p class="d split-words">{p["intro"]}</p></section>
<section class="w-facts stats" style="--n:{len(p["facts"])}">{facts}</section>
{blocks(p["blocks"])}
</main>
<a class="nextp" href="{nxt["slug"]}.html" data-cursor="Next"><span class="m">Next project →</span><div class="d t">{"<br>".join(nxt["title"])}</div><img src="{img(nxt["hero"])}" alt=""></a>
<footer class="footer" style="padding-top:8vh"><div class="legal m" style="margin-top:0"><span>© 2026 Amy Hu</span><a href="../index.html">Home</a><a href="../../">Full portfolio</a></div></footer>
<script src="../site/vendor/gsap.min.js"></script>
<script src="../site/vendor/ScrollTrigger.min.js"></script>
<script src="../site/vendor/lenis.min.js"></script>
<script src="../site/work.js"></script>
</body>
</html>
'''

exec(open(os.path.join(os.path.dirname(__file__), 'work_content.py')).read())

ORDER = ['tactile-books', 'miniature-house', 'physics-of-baking', 'guzheng-taekwondo', 'physics-tournaments', 'metallic-glass', 'optics',
         'modelling', 'smarthearing', 'curawave', 'lingtong']
PAGES.sort(key=lambda p: ORDER.index(p['slug']))

# Every page is now hand-built by art_pages.py or research_pages.py; PAGES remains the content archive.
BESPOKE = {'tactile-books', 'miniature-house', 'physics-of-baking', 'guzheng-taekwondo',  # art_pages.py
           'physics-tournaments', 'metallic-glass', 'optics', 'modelling', 'smarthearing', 'curawave', 'lingtong'}  # research_pages.py

for i, p in enumerate(PAGES):
    nxt = PAGES[(i + 1) % len(PAGES)]
    if p['slug'] in BESPOKE: continue
    open(OUT + p['slug'] + '.html', 'w').write(page(p, nxt))
    print('wrote', p['slug'])
