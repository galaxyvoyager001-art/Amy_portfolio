"""Essay-style pages for the two handmade books (docs/work/tactile-books.html, physics-of-baking.html).
These are written by hand rather than from work_content.py; build_work.py skips their slugs."""
import os, re
HERE = os.path.dirname(__file__)
src = open(os.path.join(HERE, 'build_work.py')).read()
NAV = re.search(r"NAV = '''(.*?)'''", src, re.S).group(1)
OUT = '/home/user/Amy_portfolio/docs/work/'

def wrap(slug, title, desc, og, body_cls, body, nxt_href, nxt_title, nxt_img):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Amy Hu</title>
<meta name="description" content="{desc}">
<meta property="og:image" content="{og}">
<link rel="stylesheet" href="../site/style.css">
<link rel="stylesheet" href="../site/work.css">
<link rel="stylesheet" href="../site/art.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22%3E%3Ccircle cx=%2216%22 cy=%2216%22 r=%2214%22 fill=%22%23FF5A1F%22/%3E%3C/svg%3E">
</head>
<body class="work {body_cls}">
{NAV}
<main>
{body}
</main>
<a class="nextp" href="{nxt_href}" data-cursor="Next"><span class="m">Next project →</span><div class="d t">{nxt_title}</div><img src="{nxt_img}" alt=""></a>
<footer class="footer" style="padding-top:8vh"><div class="legal m" style="margin-top:0"><span>© 2026 Amy Hu</span><a href="../index.html">Home</a><a href="../portfolio/index.html">Full portfolio</a></div></footer>
<script src="../site/vendor/gsap.min.js"></script>
<script src="../site/vendor/ScrollTrigger.min.js"></script>
<script src="../site/vendor/lenis.min.js"></script>
<script src="../site/work.js"></script>
<script src="../site/art.js"></script>
</body>
</html>
'''

W = '../site/img/w/'
I = '../site/img/'

# ------------------------------------------------------------------ TOUCH
TOUCH = f'''
<header class="t-hero" data-spot>
  <div class="t-under"><img src="{W}kids2_hd.webp" alt="Two children reading a felt book with their fingers"></div>
  <div class="t-dark"></div>
  <span class="m t-kick">01 · Touch · an essay in six fragments</span>
  <h1 class="brl d" data-text="even without sight" aria-label="Even without sight"></h1>
  <p class="t-hint">Move slowly. This page is read the way the books are: a little at a time.</p>
  <div class="t-foot m"><span>Tactile picture books in felt &amp; braille</span><span>Care &amp; Reading · ABF Beijing</span></div>
</header>

<section class="frag">
  <span class="fn m">I.</span>
  <h2 class="fh">A question from 1688</h2>
  <p class="big split-words">In 1688 William Molyneux wrote to John Locke with a puzzle. A man born blind has learned to tell a cube from a sphere by touch. If he were suddenly given sight, could he name them <em>just by looking?</em></p>
  <div class="cols">
    <p>Philosophers argued about it for three hundred years. In 2011, researchers finally asked patients who had just gained their sight after surgery. The answer, at first, was no: knowing a shape by hand did not mean knowing it by eye.</p>
    <p>Our books asked the question the other way round. A picture book is made for eyes. <b>What is a triangle to a hand that has never seen one drawn?</b> Every page of the Kingdom of Shapes is an attempt at an answer.</p>
  </div>
</section>

<section class="hands" data-hands>
  <div class="hands-in">
    <div class="hands-head"><span class="fn m">II.</span><h2 class="fh">Sight takes the world all at once.<br><em>Touch takes it one edge at a time.</em></h2></div>
    <div class="hands-track">
      <figure><img src="{W}cut_step_draw.webp" alt="Drawing a shape onto felt"><figcaption><b class="d">Draw</b><span>A line before there is anything to feel.</span></figcaption></figure>
      <figure><img src="{W}cut_step_measure.webp" alt="Measuring felt strips"><figcaption><b class="d">Measure</b><span>A finger is wider than a pencil. Every edge is made thicker than it looks.</span></figcaption></figure>
      <figure><img src="{W}cut_step_cut.webp" alt="Cutting felt with scissors"><figcaption><b class="d">Cut</b><span>Felt, not paper: it has to survive being read a thousand times.</span></figcaption></figure>
      <figure><img src="{W}cut_step_glue.webp" alt="Fixing the braille story card"><figcaption><b class="d">Fix</b><span>The braille card goes opposite the scene, so the story and the shape are read side by side.</span></figcaption></figure>
    </div>
  </div>
</section>

<section class="frag">
  <span class="fn m">III.</span>
  <h2 class="fh">The Kingdom of Shapes</h2>
  <div class="kingdom">
    <div class="ktext">
      <p>Because touch reads in sequence, a tactile book is closer to a piece of music than to a picture. So each page is a small journey with something waiting at the end of it.</p>
      <p>In the first book, <b>Jianjian the triangle</b> crosses town to a New Year concert, and every scene hides a triangle to find. In the second, <b>Fangfang the square</b> becomes something new on every page: a flying carpet, a car, a drum, a gem.</p>
      <div class="cells" data-cells aria-label="The word shape in braille"></div>
      <p class="m small">Run your cursor over the dots: “shape”, in braille.</p>
    </div>
    <div class="kpages">
      <figure class="kp"><img src="{W}page1.webp" alt="Triangle Town page with movable felt rods"><figcaption class="m">Book 1 · Triangle Town</figcaption></figure>
      <figure class="kp"><img src="{W}page7.webp" alt="A metal triangle instrument page"><figcaption class="m">Book 1 · A triangle you can strike</figcaption></figure>
      <figure class="kp"><img src="{W}fang4.webp" alt="Rattle drum page"><figcaption class="m">Book 2 · Fangfang becomes a drum</figcaption></figure>
      <figure class="kp"><img src="{W}fang7.webp" alt="Backpack buckle page"><figcaption class="m">Book 2 · Buckles to clip together</figcaption></figure>
    </div>
  </div>
</section>

<section class="vows">
  <span class="fn m">IV.</span>
  <h2 class="fh">Four rules, kept like promises</h2>
  <ol>
    <li><span class="d">Every edge can be followed.</span><em>Shapes are raised in felt strips, metal or stitching, never just printed.</em></li>
    <li><span class="d">Something always answers.</span><em>On every page, something spins, rings, clicks or moves when you find it.</em></li>
    <li><span class="d">Nothing comes loose.</span><em>Thread ends are hidden; small parts are sewn or sealed.</em></li>
    <li><span class="d">The book tells you where to go.</span><em>A raised icon on each braille card names the shape to look for next.</em></li>
  </ol>
</section>

<section class="frag mirror">
  <span class="fn m">V.</span>
  <h2 class="fh">The hand that touches is also touched</h2>
  <div class="mirror-grid">
    <div class="mtext">
      <p class="big split-words">Merleau-Ponty noticed that when your right hand touches your left, you can never quite say which one is feeling and which one is being felt.</p>
      <p>Reading together worked like that. Each volunteer in our club reads with the same child every week, year after year, more than fifty pairs in all. Over ten visits, we came to teach, and kept finding that we were the ones learning how to pay attention: to the weight of a page, the sound of a buckle, how long a small hand stays on one shape before it moves on.</p>
    </div>
    <figure class="mimg a"><img src="{W}visit_group.webp" alt="Volunteers on a visit to the NGO"></figure>
    <figure class="mimg b"><img src="{W}planet.webp" alt="Textured paintings from the My Little Planet workshop"><figcaption class="m">“My Little Planet”: painting with things you can feel</figcaption></figure>
  </div>
</section>

<section class="frag open">
  <span class="fn m">VI.</span>
  <h2 class="fh">Questions I am still holding</h2>
  <p class="lead">At the exhibition, sixty visitors read the books with their eyes closed and left notes. The best ones were not compliments.</p>
  <div class="hnotes">
    <p class="hn">“What would everyday objects feel like if I could only understand them through touch?”<span class="m">a classmate</span></p>
    <p class="hn">“Add feedback from visually impaired readers themselves.”<span class="m">a classmate</span></p>
    <p class="hn">“Explain how each texture helps a child understand the story.”<span class="m">a classmate</span></p>
    <p class="hn">“I like that you let visitors touch instead of only reading about blindness.”<span class="m">a teacher</span></p>
  </div>
  <p class="after">The second note is the one I keep. A book for blind readers should, in the end, be judged by blind readers.</p>
</section>

<section class="coda">
  <img src="{W}cut_book_closed.webp" alt="The finished felt book, closed">
  <blockquote class="d">Let the warmth of your fingertips become the light.</blockquote>
  <span class="m">From our exhibition poster</span>
</section>
'''

open(OUT + 'tactile-books.html', 'w').write(wrap(
    'tactile-books', 'Even Without Sight', 'Tactile picture books for blind children, and what making them taught me about touch.',
    W + 'cut_book_closed.webp', 'art-touch', TOUCH, 'miniature-house.html', 'A house in<br>miniature', W + 'cut_house_pano.webp'))

# ------------------------------------------------------------------ TASTE
MONTHS = [
    ('Jan', 'Simplicity', '08', 'Coconut balls', 'Four ingredients. Egg white sets at 62 °C and holds the rest together.'),
    ('Feb', 'Patience', '10', 'Croissants', 'Fold, chill, fold again. Layers cannot be hurried into being.'),
    ('Mar', 'Growth', '12', 'Bread', 'Yeast makes the gas; gluten decides how much of it stays.'),
    ('Apr', 'Renewal', '14', 'Lemon cheesecake', 'An emulsion: two things that would rather separate, held in one smooth body.'),
    ('May', 'Delicacy', '16', 'Macarons', 'A meringue foam. Structure made almost entirely of air.'),
    ('Jun', 'Lightness', '18', 'Chiffon cake', 'Lightness is not found. It is whipped in, then protected.'),
    ('Jul', 'Calm', '20', 'Matcha scones', 'Cold butter and a light hand. Overworked dough turns tough.'),
    ('Aug', 'Precision', '22', 'Egg tarts', 'Heat travels from the outside in; a custard sets in a narrow window.'),
    ('Sep', 'Restraint', '24', 'Osmanthus mung bean cake', 'Starch sets as water leaves. Nothing added that is not needed.'),
    ('Oct', 'Playfulness', '26', 'Donuts', 'Hot oil moves heat so fast the crust forms before the inside notices.'),
    ('Nov', 'Boldness', '28', 'Basque cheesecake', 'Burnt on purpose: a steep gradient, dark outside, soft within.'),
    ('Dec', 'Warmth', '30', 'Butter cookies', 'Viscosity decides how far a cookie spreads. Butter decides how it tastes.'),
]
rows = ''.join(f'<li data-img="{W}cut_bake_{n}.webp"><span class="m mo">{m}</span><span class="vw">{v}</span><span class="rc"><b>{r}</b>{t}</span><img class="mob" src="{W}cut_bake_{n}.webp" alt="{r}"></li>' for m, v, n, r, t in MONTHS)
ring = ' · '.join(v for _, v, *_ in MONTHS) + ' · '

OVEN = [(34, 'Butter melts'), (62, 'Egg whites set'), (70, 'Starch gelatinises'), (100, 'Water becomes steam, 1,700 times its volume'), (150, 'Maillard browning'), (170, 'Sugar caramelises')]
oven = ''.join(f'<li data-t="{t}"><b class="d">{t}°</b><span>{e}</span></li>' for t, e in OVEN)

TASTE = f'''
<header class="b-hero">
  <span class="m b-kick">03 · Taste · a book I wrote, baked, photographed and designed</span>
  <div class="b-ring">
    <svg viewBox="0 0 600 600" aria-hidden="true"><defs><path id="rp" d="M300,300 m-250,0 a250,250 0 1,1 500,0 a250,250 0 1,1 -500,0"/></defs>
      <text><textPath href="#rp" textLength="1560">{ring}</textPath></text></svg>
    <img src="{I}croissant.webp" alt="A croissant from February: Patience">
  </div>
  <h1 class="d b-title"><span>The physics</span><span>of baking</span></h1>
  <p class="b-sub">Twelve months, twelve recipes, and twelve small ways of being a person.</p>
</header>

<section class="ded">
  <span class="m">Dedication</span>
  <p class="hw"><span>For my grandfather,</span><span>whose hearing challenges first taught me</span><span>to notice the quiet details of everyday life;</span></p>
  <p class="hw"><span>for my family, who filled our kitchen</span><span>with patience and warmth;</span></p>
  <p class="hw"><span>and for every curious baker who has ever found</span><span>science hidden in a whisk, a rise, or a golden crust.</span></p>
</section>

<section class="oven" data-oven>
  <div class="oven-in">
    <div class="oven-l">
      <span class="fn m">The arrow of time</span>
      <h2 class="fh">Nothing in an oven <em>goes backwards.</em></h2>
      <p>Melted chocolate sets again when it cools. A cake cannot be unbaked. Proteins that have unfolded do not fold again; a crust that has browned stays brown. Physicists call this irreversibility, and file it under the second law of thermodynamics.</p>
      <p>Heraclitus said no one steps into the same river twice. No one puts the same dough into the oven twice, either. Every bake is a one-way street, which is perhaps why it is worth paying attention while it happens.</p>
    </div>
    <div class="oven-r">
      <div class="temp d"><span data-temp>20</span><small>°C</small></div>
      <ul class="evs">{oven}</ul>
    </div>
  </div>
</section>

<section class="year">
  <div class="year-head">
    <span class="fn m">One year</span>
    <h2 class="fh">Each month, a recipe, a law of physics,<br><em>and a word to live by for thirty days.</em></h2>
    <p>The book gives every month a “personal identity theme”: a quality the recipe asks of you before it gives anything back.</p>
  </div>
  <ol class="vlist">{rows}</ol>
  <img class="vpeek" alt="" aria-hidden="true">
</section>

<section class="memory">
  <div class="mem-img"><img src="{I}art/bk_p37.webp" alt="The last page of the book, Until Next Time, with madeleines on a windowsill"></div>
  <div class="mem-txt">
    <span class="fn m">Memory &amp; method</span>
    <p class="big">In 1913, Proust tasted a madeleine dipped in tea and a whole childhood came back to him. Taste is the sense that keeps time.</p>
    <p>I wrote this book for a grandfather who hears less of the world than he used to. Recipes are one of the ways a family keeps talking when other ways get harder. The last page of the book, by no accident, is a plate of madeleines.</p>
    <blockquote class="hw2">“In every rise, crumble, and caramelised edge, there is both memory and method.”</blockquote>
  </div>
</section>

<section class="leaves">
  <div class="leaves-head"><span class="fn m">The object</span><h2 class="fh">38 pages. Every photograph, every diagram, every word.</h2></div>
  <div class="stack">
    <figure class="leaf"><img src="{I}art/bk_p05.webp" alt="Introduction page"><figcaption class="m">Introduction</figcaption></figure>
    <figure class="leaf"><img src="{I}art/bk_p10.webp" alt="February: Patience"><figcaption class="m">February · Patience</figcaption></figure>
    <figure class="leaf"><img src="{I}art/bk_p11.webp" alt="The physics of croissants"><figcaption class="m">The physics of croissants</figcaption></figure>
    <figure class="leaf"><img src="{W}book_cover.webp" alt="Cover of The Physics of Baking"><figcaption class="m">Published on Amazon KDP</figcaption></figure>
  </div>
</section>
'''

open(OUT + 'physics-of-baking.html', 'w').write(wrap(
    'physics-of-baking', 'The Physics of Baking', 'A baking book about physics, time and memory: twelve months, twelve recipes, twelve virtues.',
    W + 'book_cover.webp', 'art-taste', TASTE, 'guzheng-taekwondo.html', 'Sound &amp;<br>motion', W + 'cut_guzheng.webp'))
print('ok')
