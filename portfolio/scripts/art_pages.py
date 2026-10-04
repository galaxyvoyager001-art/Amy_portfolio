"""Essay-style pages for the crafts and arts (docs/work/: tactile-books, miniature-house, physics-of-baking, guzheng-taekwondo).
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

<section class="readpage">
  <span class="fn m">IV.</span>
  <h2 class="fh">One page, <em>read by a hand</em></h2>
  <p class="rp-lead">The waiter in a triangle tailcoat, carrying the newest drink in the Kingdom of Shapes. Hover the numbers to follow a finger across the page.</p>
  <div class="rp">
    <img src="{W}page7.webp" alt="A book spread: a metal triangle instrument on purple felt, and a braille story card">
    <button class="pin" style="--x:11%;--y:58%" data-n="1"><span class="pl"><b>Follow the edge.</b> Real metal, three corners: the shape is found before it is named.</span></button>
    <button class="pin" style="--x:38%;--y:46%" data-n="2"><span class="pl"><b>Strike it.</b> The beater is the triangle’s partner; the page answers with a ring.</span></button>
    <button class="pin" style="--x:29%;--y:34%" data-n="3"><span class="pl"><b>Nothing gets lost.</b> An elastic loop keeps the beater tied to its page.</span></button>
    <button class="pin" style="--x:66%;--y:24%" data-n="4"><span class="pl"><b>The story, in dots.</b> Braille and print sit side by side, so a blind child and a sighted parent read together.</span></button>
    <button class="pin" style="--x:94%;--y:66%" data-n="5"><span class="pl"><b>Where to go next.</b> A raised glass, one more triangle hiding in the story.</span></button>
  </div>
</section>

<section class="frag mirror">
  <span class="fn m">V.</span>
  <h2 class="fh">The hand that touches is also touched</h2>
  <div class="mirror-grid">
    <div class="mtext">
      <p class="big split-words">Merleau-Ponty noticed that when your right hand touches your left, you can never quite say which one is feeling and which one is being felt.</p>
      <p>Reading together worked like that. Each volunteer in our club reads with the same child every week, year after year, more than fifty pairs in all. Over ten visits, we came to teach, and kept finding that we were the ones learning how to pay attention: to the weight of a page, the sound of a buckle, how long a small hand stays on one shape before it moves on.</p>
    </div>
    <figure class="mimg a"><img src="{W}books_grid.webp" alt="The finished felt books, spread by spread"><figcaption class="m">The finished books, spread by spread</figcaption></figure>
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

# ------------------------------------------------------------------ SIGHT
ROOMS = [('house_d2', 'The study', 'Someone works here. Tiny printed books fill the shelves; a chair is pulled up to the desk.'),
         ('house_d1', 'The dressing room', 'A yellow towel on the rail, slippers by the basin: the morning has just happened.'),
         ('house_d3_cut', 'The living room', 'A round window, painted branches, a screen glowing with a mountain at sunset.'),
         ('house_d4', 'The kitchen', 'Tucked under the loft bed, because in a small home every corner works twice.'),
         ('house_d5_cut', 'The dining room', 'Dinner is already served. Whoever lives here is about to sit down.')]
reel = ''.join(f'<figure><img src="{W}{i}.webp" alt="{t}"><figcaption><b class="d">{t}</b><span>{c}</span></figcaption></figure>' for i, t, c in ROOMS)

SIGHT = f'''
<header class="h-hero" data-shrink>
  <div class="h-pin">
    <span class="m h-kick">02 · Sight · an essay on scale</span>
    <h1 class="d h-title"><span>A house</span><span>in miniature</span></h1>
    <img class="h-house" src="{W}cut_house_pano.webp" alt="The miniature house, five rooms on one floor">
    <p class="h-sub">Five rooms, one desk, more than two hundred parts made by hand.</p>
  </div>
</header>

<section class="frag">
  <span class="fn m">I.</span>
  <h2 class="fh">A mustard seed <em>holds a mountain</em></h2>
  <p class="big split-words">“The cleverer I am at miniaturizing the world, the better I possess it.” Gaston Bachelard wrote that in <em>The Poetics of Space</em>, in a chapter about tiny things.</p>
  <div class="cols">
    <p>A Buddhist phrase says the same thing more boldly: 芥子纳须弥, a mustard seed can hold Mount Sumeru. Making this house felt like testing that idea with tweezers. How much of a home survives when everything is shrunk onto a desk?</p>
    <p>The answer, it turns out, is everything that matters: not the size of the rooms but the traces of the person in them. A towel left on the rail. A chair pulled out. Dinner on the table, still waiting.</p>
  </div>
</section>

<section class="loupe-sec">
  <span class="fn m">II.</span>
  <h2 class="fh">Look closer</h2>
  <div class="loupe" data-loupe style="--img:url({W}house_d2.webp)">
    <img src="{W}house_d2.webp" alt="The study, with a bookcase, desk and chair">
    <div class="lens" aria-hidden="true"></div>
  </div>
  <p class="loupe-cap">Move the lens across the study. At this scale, a book is a fold of paper and a lamp is a bead, and the question is never “is it accurate?” but “does it feel lived in?”</p>
</section>

<section class="hands rooms" data-hands>
  <div class="hands-in">
    <div class="hands-head"><span class="fn m">III.</span><h2 class="fh">Five rooms, <em>one life</em></h2></div>
    <div class="hands-track">{reel}</div>
  </div>
</section>

<section class="moon" data-moon>
  <div class="moon-in">
    <div class="moon-hole"><img src="{W}house_d7.webp" alt="The whole house seen through a round window"></div>
    <div class="moon-txt">
      <span class="fn m">IV. 借景 · borrowed scenery</span>
      <p>Chinese gardens are often small, so they borrow. A round <i>moon window</i> frames a view beyond the wall, and a courtyard a few steps wide suddenly holds a whole landscape.</p>
      <p>The living room does the same. A few centimetres of wall open onto painted branches and a mountain at sunset. Scroll, and the window opens onto the house.</p>
    </div>
  </div>
</section>

<section class="frag build">
  <span class="fn m">V.</span>
  <h2 class="fh">How it was built</h2>
  <ol class="hsteps">
    <li><b class="d">Plan the floor</b><span>Five rooms on one level, with the bed lofted above the kitchen.</span></li>
    <li><b class="d">Build the shell</b><span>Walls, floor and loft must be square, or nothing inside sits straight.</span></li>
    <li><b class="d">Make the furniture</b><span>Bookcase, desk, bed, sofa, cabinets: piece by piece, with tweezers and glue.</span></li>
    <li><b class="d">Dress every room</b><span>Bedding, a towel, food on the plates: the details that make it lived in.</span></li>
  </ol>
  <div class="tiny">
    <figure><img src="{W}house_d8_cut.webp" alt="A tea set smaller than a fingernail"><figcaption class="m">A tea set smaller than a fingernail</figcaption></figure>
    <figure><img src="{W}house_d5_cut.webp" alt="A dinner table, fully set"><figcaption class="m">Dinner, already served</figcaption></figure>
  </div>
</section>

<section class="coda">
  <blockquote class="d">Making it small is easy. Making it <em>believable</em> is the work.</blockquote>
</section>
'''

open(OUT + 'miniature-house.html', 'w').write(wrap(
    'miniature-house', 'A House in Miniature', 'A miniature home built by hand, and an essay on scale, detail and borrowed scenery.',
    W + 'cut_house_pano.webp', 'art-sight', SIGHT, 'physics-of-baking.html', 'The physics<br>of baking', W + 'book_cover.webp'))

# ------------------------------------------------------------------ SOUND & MOTION
SOUND = f'''
<header class="s-hero" data-strings>
  <svg class="strings" aria-hidden="true"></svg>
  <span class="m s-kick">04 · Sound &amp; Motion · an essay on stillness</span>
  <h1 class="d s-title"><span>Sound &amp;</span><span>motion</span></h1>
  <img class="s-zheng" src="{W}cut_guzheng.webp" alt="Amy playing the guzheng">
  <div class="s-foot"><p>Twenty-one strings. Run your cursor across them.</p><button class="snd m" type="button" aria-pressed="false">Sound off</button></div>
</header>

<section class="frag">
  <span class="fn m">I. 大音希声</span>
  <h2 class="fh">The greatest sound <em>is barely heard</em></h2>
  <p class="big split-words">Laozi wrote that the greatest music is faint, almost silent. Two and a half thousand years later, John Cage walked onto a stage in 1952 and played nothing at all for four minutes and thirty-three seconds.</p>
  <div class="cols">
    <p>On the guzheng, plucking a string is only half of a note. The left hand presses, bends and shakes the string after it sounds, so the pitch keeps moving as it fades. Much of the music lives in the decay, and in the rest that follows it.</p>
    <p>I play the 21-string zither as a soloist, in duets and with an ensemble, and I sing. I performed at our school gala in the spring of Grade 10 and at the school’s public performance in the autumn of Grade 11.</p>
  </div>
</section>

<section class="stage">
  <figure class="st-a"><img src="{W}guzheng_duo.webp" alt="A guzheng duet on stage under a projected mountain sky"><figcaption class="m">Duet · school gala</figcaption></figure>
  <figure class="st-b"><img src="{W}ensemble1.webp" alt="A guzheng ensemble performing outdoors"><figcaption class="m">Ensemble · outdoors</figcaption></figure>
  <figure class="st-c"><img src="{W}sing.webp" alt="Singing on stage with friends"><figcaption class="m">Voice</figcaption></figure>
</section>

<section class="still" data-still>
  <div class="still-in">
    <img class="still-fig" src="{W}cut_tkd2.webp" alt="Amy in a taekwondo stance">
    <div class="still-txt">
      <span class="fn m">II. 静中有动</span>
      <h2 class="fh">Every kick <em>begins standing still</em></h2>
      <p class="lines"><span>A Chinese saying: in stillness there is motion,</span><span>and in motion, stillness.</span></p>
      <p>Eight years of taekwondo taught me that the fastest movement starts from the calmest stance: weight settled, eyes level, breath held for one beat. A kick that is hurried arrives late.</p>
    </div>
  </div>
</section>

<section class="mat">
  <img src="{W}tkd_match.webp" alt="A competition bout in Beijing">
  <div class="mat-stats">
    <div class="stat"><b class="d" data-count="8">0</b><span>years on the mat</span></div>
    <div class="stat"><b class="d">Gold</b><span>Beijing competition</span></div>
    <div class="stat"><b class="d">Black</b><span>belt</span></div>
    <div class="stat"><b class="d" data-count="50" data-suffix="+">0</b><span>younger students coached</span></div>
  </div>
</section>

<section class="frag teach">
  <span class="fn m">III.</span>
  <div class="teach-grid">
    <div>
      <h2 class="fh">To teach a movement, <em>slow it down</em></h2>
      <p>Since Grade 5 I have been an assistant instructor at Shangdi Youth Taekwondo Academy, coaching more than fifty younger students in forms, kicks, sparring and discipline.</p>
      <p>Teaching means taking a movement I can do without thinking and slowing it down until a younger student can copy it: where the foot turns, when the hip opens, where the eyes go. It is the same patience a phrase on the guzheng asks for.</p>
    </div>
    <figure><img src="{W}tkd_teaching.webp" alt="Leading a class of young students at sunset"></figure>
  </div>
</section>

'''

open(OUT + 'guzheng-taekwondo.html', 'w').write(wrap(
    'guzheng-taekwondo', 'Sound & Motion', 'Guzheng and taekwondo: an essay on stillness, sound and motion.',
    W + 'cut_guzheng.webp', 'art-sound', SOUND, 'physics-tournaments.html', 'Coupled<br>pendulums', W + 'cut_ee_rig.webp'))
print('ok')
