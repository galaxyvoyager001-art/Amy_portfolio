import math, random, cairosvg

class Sheet:
    def __init__(self, w=1200, h=900, seed=1):
        self.w, self.h = w, h
        self.r = random.Random(seed)
        self.defs = []
        self.layers = {'wash': [], 'hatch': [], 'cons': [], 'ink': [], 'text': []}
        self.clip_id = 0

    def j(self, a=1.4):
        return self.r.uniform(-a, a)

    # ---------- pen strokes ----------
    def line(self, x1, y1, x2, y2, w=1.6, color='#1d1d22', over=7, passes=2, layer='ink', op=0.92):
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        ux, uy = dx / L, dy / L
        for p in range(passes):
            o1 = self.r.uniform(0, over) if p == 0 else self.r.uniform(-2, over * 0.6)
            o2 = self.r.uniform(0, over)
            ax, ay = x1 - ux * o1 + self.j(), y1 - uy * o1 + self.j()
            bx, by = x2 + ux * o2 + self.j(), y2 + uy * o2 + self.j()
            # slight bow
            mx, my = (ax + bx) / 2 + (-uy) * self.j(L * 0.006 + 0.8), (ay + by) / 2 + ux * self.j(L * 0.006 + 0.8)
            sw = w * (1 if p == 0 else 0.6)
            self.layers[layer].append(
                f'<path d="M{ax:.1f} {ay:.1f} Q{mx:.1f} {my:.1f} {bx:.1f} {by:.1f}" fill="none" stroke="{color}" '
                f'stroke-width="{sw:.2f}" stroke-linecap="round" opacity="{op if p == 0 else op * 0.55:.2f}"/>')

    def poly(self, pts, closed=True, **kw):
        n = len(pts)
        for i in range(n if closed else n - 1):
            a, b = pts[i], pts[(i + 1) % n]
            self.line(a[0], a[1], b[0], b[1], **kw)

    def circle(self, cx, cy, r, w=1.5, color='#1d1d22', passes=2, layer='ink'):
        for p in range(passes):
            pts = []
            start = self.r.uniform(0, 2 * math.pi)
            span = 2 * math.pi + self.r.uniform(0.15, 0.5)
            for k in range(40):
                t = start + span * k / 39
                rr = r + self.j(r * 0.025 + 0.6)
                pts.append((cx + rr * math.cos(t), cy + rr * math.sin(t)))
            d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
            self.layers[layer].append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w * (1 if p == 0 else .6):.2f}" stroke-linecap="round" opacity="{.9 if p == 0 else .5}"/>')

    def cons(self, x1, y1, x2, y2):
        self.line(x1, y1, x2, y2, w=0.7, color='#7a7f8c', over=40, passes=1, layer='cons', op=0.45)

    def dash(self, x1, y1, x2, y2, color='#3a3a44', w=1.0):
        self.layers['cons'].append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{w}" stroke-dasharray="6 6" opacity=".7"/>')

    # ---------- marker wash ----------
    def wash(self, pts, color, op=0.55, off=5):
        ox, oy = self.r.uniform(-off, off), self.r.uniform(-off, off)
        d = 'M' + ' L'.join(f'{x + ox + self.j(3):.1f} {y + oy + self.j(3):.1f}' for x, y in pts) + ' Z'
        self.layers['wash'].append(f'<path d="{d}" fill="{color}" opacity="{op}"/>')
        # streaks typical of markers
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        self.clip_id += 1
        cid = f'c{self.clip_id}'
        dd = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ' Z'
        self.defs.append(f'<clipPath id="{cid}"><path d="{dd}"/></clipPath>')
        g = []
        x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
        step = 9
        k = x0 - (y1 - y0)
        while k < x1:
            g.append(f'<line x1="{k:.1f}" y1="{y1 + 4:.1f}" x2="{k + (y1 - y0) * 0.9:.1f}" y2="{y0 - 4:.1f}" stroke="{color}" stroke-width="{self.r.uniform(5, 9):.1f}" opacity="{self.r.uniform(.12, .25):.2f}"/>')
            k += step * self.r.uniform(1.1, 2.2)
        self.layers['wash'].append(f'<g clip-path="url(#{cid})">{"".join(g)}</g>')

    def hatch(self, pts, gap=7, angle=45, color='#1d1d22', w=0.8):
        self.clip_id += 1
        cid = f'c{self.clip_id}'
        dd = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ' Z'
        self.defs.append(f'<clipPath id="{cid}"><path d="{dd}"/></clipPath>')
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
        R = max(max(xs) - min(xs), max(ys) - min(ys))
        a = math.radians(angle)
        g = []
        t = -R
        while t < R:
            px, py = cx + t * math.cos(a + math.pi / 2), cy + t * math.sin(a + math.pi / 2)
            g.append(f'<line x1="{px - R * math.cos(a) + self.j():.1f}" y1="{py - R * math.sin(a) + self.j():.1f}" x2="{px + R * math.cos(a):.1f}" y2="{py + R * math.sin(a):.1f}" stroke="{color}" stroke-width="{w}" opacity=".6"/>')
            t += gap * self.r.uniform(0.85, 1.15)
        self.layers['hatch'].append(f'<g clip-path="url(#{cid})">{"".join(g)}</g>')

    # ---------- annotation ----------
    def text(self, x, y, s, size=17, color='#1d1d22', font='Architects Daughter', anchor='start', rot=0, weight='normal'):
        s = s.replace('&', '&amp;').replace('<', '&lt;')
        tr = f' transform="rotate({rot} {x} {y})"' if rot else ''
        self.layers['text'].append(f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}"{tr}>{s}</text>')

    def leader(self, x1, y1, x2, y2, label, size=16, anchor='start'):
        self.layers['ink'].append(f'<circle cx="{x1}" cy="{y1}" r="3.2" fill="#1d1d22"/>')
        self.line(x1, y1, x2, y2, w=0.9, over=0, passes=1)
        self.line(x2, y2, x2 + (60 if anchor == 'start' else -60), y2, w=0.9, over=0, passes=1)
        self.text(x2 + (4 if anchor == 'start' else -4), y2 - 6, label, size=size, anchor=anchor)

    def tag(self, x, y, n, color='#E8552B'):
        self.circle(x, y, 13, w=1.3)
        self.layers['wash'].append(f'<circle cx="{x + 1.5}" cy="{y + 1.5}" r="12" fill="{color}" opacity=".55"/>')
        self.text(x, y + 6, str(n), size=16, anchor='middle')

    def dim(self, x1, y1, x2, y2, label, off=0):
        self.line(x1, y1, x2, y2, w=0.8, over=10, passes=1)
        L = math.hypot(x2 - x1, y2 - y1) or 1
        nx, ny = -(y2 - y1) / L, (x2 - x1) / L
        for (px, py) in [(x1, y1), (x2, y2)]:
            self.line(px - nx * 7 + (x2 - x1) / L * -5, py - ny * 7 + (y2 - y1) / L * -5, px + nx * 7 + (x2 - x1) / L * 5, py + ny * 7 + (y2 - y1) / L * 5, w=1.1, over=0, passes=1)
        mx, my = (x1 + x2) / 2 + nx * (14 + off), (y1 + y2) / 2 + ny * (14 + off)
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        if ang > 90 or ang < -90:
            ang += 180
        self.text(mx, my + 5, label, size=15, anchor='middle', rot=round(ang, 1))

    def arrow(self, x1, y1, x2, y2, w=1.4, color='#1d1d22'):
        self.line(x1, y1, x2, y2, w=w, over=0, passes=1, color=color)
        a = math.atan2(y2 - y1, x2 - x1)
        for s in (1, -1):
            self.line(x2, y2, x2 - 13 * math.cos(a + s * 0.45), y2 - 13 * math.sin(a + s * 0.45), w=w, over=0, passes=1, color=color)

    def title_block(self, title, sub, no):
        W, H = self.w, self.h
        self.line(40, H - 92, W - 40, H - 92, w=1.2, over=14)
        self.text(48, H - 52, title, size=27)
        self.text(48, H - 24, sub, size=15, color='#4a4a55')
        self.text(W - 48, H - 52, no, size=27, anchor='end')
        self.text(W - 48, H - 24, 'TACTILE BOOK PROJECT · A. HU', size=13, anchor='end', color='#4a4a55')

    def svg(self):
        grain = ''.join(f'<circle cx="{self.r.uniform(0, self.w):.0f}" cy="{self.r.uniform(0, self.h):.0f}" r="{self.r.uniform(.4, 1.1):.1f}" fill="#b9ae98" opacity="{self.r.uniform(.15, .4):.2f}"/>' for _ in range(900))
        body = ''.join(self.layers['cons'] + self.layers['wash'] + self.layers['hatch'] + self.layers['ink'] + self.layers['text'])
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">'
                f'<defs>{"".join(self.defs)}</defs><rect width="{self.w}" height="{self.h}" fill="#FBF8F1"/>{grain}{body}</svg>')

    def save(self, path):
        cairosvg.svg2png(bytestring=self.svg().encode(), write_to=path, output_width=self.w * 2, output_height=self.h * 2)


NAVY = '#3B4FA8'; ORANGE = '#F07A3A'; TEAL = '#5BC4B4'; PINK = '#EE8FB5'; GREEN = '#52B36B'; RED = '#E0533F'; YEL = '#F4C443'; GREY = '#9AA0AA'; PURP = '#9B6CC9'


def iso(x, y, z, ox, oy, s=1.0):
    c, sn = math.cos(math.radians(30)), math.sin(math.radians(30))
    return (ox + (x - y) * c * s, oy + (x + y) * sn * s - z * s)


# ===== Sheet 1: plan of spread 01 =====
def sheet1(path):
    S = Sheet(seed=11)
    S.cons(60, 150, 1140, 150); S.cons(60, 600, 1140, 600); S.cons(140, 90, 140, 680); S.cons(1060, 90, 1060, 680)
    L = (140, 150, 590, 600); R = (610, 150, 1060, 600)
    S.wash([(L[0], L[1]), (L[2], L[1]), (L[2], L[3]), (L[0], L[3])], NAVY, .38)
    S.wash([(R[0], R[1]), (R[2], R[1]), (R[2], R[3]), (R[0], R[3])], TEAL, .38)
    for (a, b, c, d) in (L, R):
        S.poly([(a, b), (c, b), (c, d), (a, d)], w=1.8)
    S.line(600, 130, 600, 620, w=1.2)
    S.text(600, 122, 'SPINE · SEWN', size=13, anchor='middle')
    # felt strips forming triangles (drawn as long thin bars)
    def bar(p, q, col, wdt=14):
        L_ = math.hypot(q[0] - p[0], q[1] - p[1]); nx, ny = -(q[1] - p[1]) / L_ * wdt / 2, (q[0] - p[0]) / L_ * wdt / 2
        pts = [(p[0] + nx, p[1] + ny), (q[0] + nx, q[1] + ny), (q[0] - nx, q[1] - ny), (p[0] - nx, p[1] - ny)]
        S.wash(pts, col, .8, off=2); S.poly(pts, w=1.2)
    bar((200, 560), (300, 260), PINK); bar((300, 260), (330, 560), ORANGE); bar((190, 555), (340, 560), GREEN)
    bar((360, 330), (450, 330), ORANGE); bar((450, 330), (405, 250), YEL); bar((405, 250), (360, 330), RED)
    bar((400, 560), (560, 400), PINK); bar((560, 400), (560, 560), NAVY); bar((560, 560), (400, 560), GREEN)
    # cross tabs
    for (x, y, a) in [(255, 410, 20), (405, 300, 0), (500, 480, -45)]:
        S.wash([(x - 30, y - 8), (x + 30, y - 8), (x + 30, y + 8), (x - 30, y + 8)], YEL, .85, off=1); S.poly([(x - 30, y - 8), (x + 30, y - 8), (x + 30, y + 8), (x - 30, y + 8)], w=1)
    # title strip and spinning top
    S.poly([(170, 175), (420, 175), (420, 210), (170, 210)], w=1.2); S.text(295, 199, 'TITLE STRIP — PRINT + BRAILLE', size=12, anchor='middle')
    S.circle(560, 182, 22, w=1.5); S.wash([(540, 165), (580, 165), (580, 200), (540, 200)], ORANGE, .6)
    S.poly([(540, 214), (580, 214), (560, 240)], w=1.1)
    # card
    S.poly([(640, 200), (1030, 200), (1030, 560), (640, 560)], w=1.5)
    S.wash([(640, 200), (1030, 200), (1030, 560), (640, 560)], '#FFFFFF', .7)
    for row in range(5):
        for k in range(16):
            if S.r.random() < .55:
                S.layers['ink'].append(f'<circle cx="{670 + k * 21 + (k % 2) * 4}" cy="{240 + row * 34}" r="2.6" fill="#555"/>')
    for row in range(4):
        S.line(670, 420 + row * 22, 670 + S.r.uniform(160, 300), 420 + row * 22, w=1.1, color='#8a8a95', over=0, passes=1)
    S.poly([(940, 535), (1000, 535), (970, 470)], w=2)
    S.hatch([(940, 535), (1000, 535), (970, 470)], gap=5)
    # dimensions (relative, no invented numbers)
    S.dim(140, 640, 590, 640, 'W  (ONE PAGE)'); S.dim(610, 640, 1060, 640, 'W')
    S.dim(1090, 150, 1090, 600, 'H = W  · SQUARE PAGE')
    # notes
    S.leader(300, 260, 250, 110, 'FELT STRIPS = SIDES TO TRACE')
    S.leader(560, 182, 700, 110, 'SPINNING TOP · LOCKS INTO TRIANGLE LOOP')
    S.leader(970, 500, 1000, 700, 'RAISED-LINE ICON', anchor='end')
    S.leader(800, 270, 860, 700, 'STORY IN BRAILLE', anchor='end')
    S.text(170, 760, '"MY NAME IS JIANJIAN. I LIVE IN TRIANGLE TOWN."', size=18, color='#3B4FA8')
    S.title_block('PLAN — SPREAD 01, TRIANGLE TOWN', 'SCENE (LEFT) FACES STORY CARD (RIGHT) · THREE TRIANGLES, THREE SIZES', 'A-01')
    S.save(path)


# ===== Sheet 2: exploded axonometric =====
def sheet2(path):
    S = Sheet(seed=22)
    ox, oy, s = 500, 330, 0.82
    layers = [(-120, 'BASE FELT · 2 LAYERS', NAVY), (-15, 'FELT STRIPS · SEWN DOWN', ORANGE), (85, 'TRIANGLE LOOP + SILICONE SLEEVE', PINK), (185, 'BRAILLE CARD (FACING PAGE)', TEAL)]
    P = 300
    for i, (z, label, col) in enumerate(layers):
        a = iso(0, 0, z, ox, oy, s); b = iso(P, 0, z, ox, oy, s); c = iso(P, P, z, ox, oy, s); d = iso(0, P, z, ox, oy, s)
        if i == 0:
            # base slab with thickness
            a2, b2, c2, d2 = [iso(x, y, z - 18, ox, oy, s) for (x, y) in [(0, 0), (P, 0), (P, P), (0, P)]]
            S.wash([a, b, c, d], col, .45); S.poly([a, b, c, d], w=1.6); S.wash([b, c, c2, b2], col, .55); S.wash([c, d, d2, c2], col, .75)
            S.hatch([c, d, d2, c2], gap=6, angle=60)
            S.poly([b, c, c2, b2], w=1.4); S.poly([c, d, d2, c2], w=1.4)
        if i == 1:
            for (p, q, cc) in [((40, 260), (150, 40), PINK), ((150, 40), (260, 260), GREEN), ((260, 260), (40, 260), YEL)]:
                pa = iso(p[0], p[1], z, ox, oy, s); pb = iso(q[0], q[1], z, ox, oy, s)
                pa2 = iso(p[0], p[1], z + 10, ox, oy, s); pb2 = iso(q[0], q[1], z + 10, ox, oy, s)
                S.wash([pa, pb, pb2, pa2], cc, .85, off=1); S.poly([pa, pb, pb2, pa2], w=1.3)
            S.poly([a, b, c, d], w=0.8, color='#8a8a95')
        elif i == 2:
            tri = [iso(x, y, z, ox, oy, s) for (x, y) in [(220, 30), (280, 30), (250, 90)]]
            S.wash(tri, col, .7); S.poly(tri, w=1.5)
            t = iso(250, 60, z + 60, ox, oy, s)
            S.circle(t[0], t[1], 26, w=1.6); S.wash([(t[0] - 24, t[1] - 22), (t[0] + 24, t[1] - 22), (t[0] + 24, t[1] + 22), (t[0] - 24, t[1] + 22)], ORANGE, .6)
            S.line(t[0], t[1] + 26, tri[2][0], tri[2][1] - 10, w=1.4)
            S.poly([a, b, c, d], w=0.8, color='#8a8a95')
        elif i == 3:
            S.wash([a, b, c, d], col, .45); S.poly([a, b, c, d], w=1.6)
            inner = [iso(x, y, z, ox, oy, s) for (x, y) in [(30, 30), (270, 30), (270, 270), (30, 270)]]
            S.wash(inner, '#FFFFFF', .8); S.poly(inner, w=1.2)
            for k in range(30):
                px, py = iso(50 + (k % 10) * 20, 50 + (k // 10) * 22, z, ox, oy, s)
                S.layers['ink'].append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2.3" fill="#555"/>')
        else:
            S.poly([a, b, c, d], w=1.6)
        # alignment lines between layers
        if i < len(layers) - 1:
            for (x, y) in [(0, 0), (P, 0), (P, P), (0, P)]:
                p1 = iso(x, y, z, ox, oy, s); p2 = iso(x, y, layers[i + 1][0], ox, oy, s)
                S.dash(p1[0], p1[1], p2[0], p2[1])
        lab = iso(P, 0, z, ox, oy, s)
        S.tag(lab[0] + 40, lab[1] - 10, 4 - i)
        S.text(lab[0] + 64, lab[1] - 4, label, size=17)
    S.cons(80, 700, 1120, 700)
    S.arrow(150, 560, 150, 360); S.text(160, 470, 'ASSEMBLY ORDER', size=14, rot=-90)
    S.text(70, 120, 'EXPLODED AXONOMETRIC', size=34)
    S.text(70, 152, 'HOW ONE SPREAD IS BUILT, BOTTOM TO TOP', size=16, color='#4a4a55')
    S.text(760, 760, 'NOTHING LOOSE: EVERY SMALL PART IS SEWN', size=16, color='#B5432A')
    S.text(760, 784, 'OR SEALED SO IT CANNOT BE SWALLOWED', size=16, color='#B5432A')
    S.title_block('AXO — PAGE ASSEMBLY', 'BASE · STRIPS · MOVING PART · BRAILLE CARD', 'A-02')
    S.save(path)


# ===== Sheet 3: section through tree page =====
def sheet3(path):
    S = Sheet(seed=33)
    # elevation (top) of tree
    cx = 330
    tiers = [(cx, 200, 110, 300), (cx, 280, 150, 390), (cx, 360, 190, 490)]
    cols = [GREEN, '#3FA35A', GREEN]
    for (x, top, half, base), col in zip(tiers, cols):
        pts = [(x, top), (x + half, base), (x - half, base)]
        S.wash(pts, col, .7); S.poly(pts, w=1.6)
    S.poly([(cx - 22, 490), (cx + 22, 490), (cx + 22, 530), (cx - 22, 530)], w=1.4); S.hatch([(cx - 22, 490), (cx + 22, 490), (cx + 22, 530), (cx - 22, 530)], gap=5)
    star = [(cx + 22 * math.cos(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else .45), 180 + 22 * math.sin(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else .45)) for k in range(10)]
    S.wash(star, YEL, .9); S.poly(star, w=1.2)
    for k in range(7):
        x = cx - 120 + k * 40; y = 382 + (k % 2) * 4
        S.layers['ink'].append(f'<circle cx="{x}" cy="{y}" r="5" fill="#F4C443" stroke="#1d1d22" stroke-width="1"/>')
    S.dash(cx - 230, 382, cx + 230, 382, color='#B5432A', w=1.4)
    S.text(cx + 240, 378, 'A', size=24); S.text(cx - 250, 378, 'A', size=24, anchor='end')
    S.poly([(cx + 120, 500), (cx + 200, 500), (cx + 200, 560), (cx + 120, 560)], w=1.4); S.wash([(cx + 120, 500), (cx + 200, 500), (cx + 200, 560), (cx + 120, 560)], RED, .6)
    S.line(cx + 160, 500, cx + 160, 560, w=1); S.line(cx + 120, 530, cx + 200, 530, w=1)
    S.text(cx, 610, 'ELEVATION', size=20, anchor='middle')
    # section (right)
    x0, y0 = 660, 300
    S.cons(620, y0, 1150, y0)
    S.poly([(x0, y0), (1120, y0), (1120, y0 + 22), (x0, y0 + 22)], w=1.6); S.hatch([(x0, y0), (1120, y0), (1120, y0 + 22), (x0, y0 + 22)], gap=5, angle=45)
    S.text(x0, y0 + 48, 'BASE FELT', size=14)
    S.poly([(x0 + 40, y0 - 14), (1080, y0 - 14), (1080, y0), (x0 + 40, y0)], w=1.3); S.wash([(x0 + 40, y0 - 14), (1080, y0 - 14), (1080, y0), (x0 + 40, y0)], GREEN, .7)
    S.text(x0 + 140, y0 + 48, 'LAYER 1 (GREEN, ABOVE BASE)', size=14)
    # LED string
    for k in range(9):
        S.layers['ink'].append(f'<circle cx="{x0 + 70 + k * 42}" cy="{y0 - 24}" r="6" fill="#F4C443" stroke="#1d1d22" stroke-width="1.1"/>')
    S.line(x0 + 60, y0 - 24, x0 + 430, y0 - 24, w=1.0, over=0)
    # velcro
    S.poly([(x0 + 40, y0 - 38), (x0 + 110, y0 - 38), (x0 + 110, y0 - 30), (x0 + 40, y0 - 30)], w=1); S.hatch([(x0 + 40, y0 - 38), (x0 + 110, y0 - 38), (x0 + 110, y0 - 30), (x0 + 40, y0 - 30)], gap=3, angle=0)
    # layer 2 lifting flap
    hx, hy = x0 + 40, y0 - 40
    flap = [(hx, hy), (hx + 400 * math.cos(math.radians(-24)), hy + 400 * math.sin(math.radians(-24))), (hx + 400 * math.cos(math.radians(-24)) + 6, hy + 400 * math.sin(math.radians(-24)) + 14), (hx + 6, hy + 14)]
    S.wash(flap, '#3FA35A', .7); S.poly(flap, w=1.5)
    S.dash(hx + 6, hy + 12, hx + 420, hy + 12)
    a1 = hx + 300
    S.layers['ink'].append(f'<path d="M{a1} {hy + 6} A300 300 0 0 0 {hx + 300 * math.cos(math.radians(-20)):.1f} {hy + 300 * math.sin(math.radians(-20)):.1f}" fill="none" stroke="#B5432A" stroke-width="1.6"/>')
    S.text(a1 + 20, hy - 60, 'LIFTS', size=16, color='#B5432A')
    # switch under gift box
    S.poly([(1000, y0 - 50), (1070, y0 - 50), (1070, y0 - 14), (1000, y0 - 14)], w=1.4); S.wash([(1000, y0 - 50), (1070, y0 - 50), (1070, y0 - 14), (1000, y0 - 14)], RED, .6)
    S.poly([(1020, y0 - 30), (1050, y0 - 30), (1050, y0 - 18), (1020, y0 - 18)], w=1)
    S.text(890, 400, 'SECTION A–A', size=24)
    S.leader(x0 + 75, y0 - 38, 700, 470, 'VELCRO HOLDS LAYER 2')
    S.leader(x0 + 240, y0 - 24, 820, 520, 'LED STRING, HIDDEN')
    S.leader(1035, y0 - 24, 1040, 580, 'SWITCH UNDER THE GIFT', anchor='end')
    S.leader(cx + 160, 530, 600, 700, 'GIFT BOX = SWITCH COVER', anchor='end')
    S.text(70, 110, 'A SURPRISE UNDER THE BRANCHES', size=30)
    S.text(70, 140, 'LIFT LAYER 2 → LIGHTS COME ON', size=16, color='#4a4a55')
    S.title_block('SECTION — THE CHRISTMAS TREE PAGE', 'LAYERED FELT · VELCRO HINGE · HIDDEN LED STRING', 'A-03')
    S.save(path)


# ===== Sheet 4: Fangfang shape sequence =====
def sheet4(path):
    S = Sheet(seed=44)
    S.text(70, 110, 'BOOK 2 · FANGFANG CHANGES SHAPE', size=32)
    S.text(70, 140, 'ONE SQUARE, PUSHED, STRETCHED AND CUT, PAGE BY PAGE', size=16, color='#4a4a55')
    S.cons(60, 330, 1140, 330)
    shapes = [
        ('SQUARE', [(0, 0), (110, 0), (110, 110), (0, 110)], RED),
        ('RECTANGLE', [(0, 25), (150, 25), (150, 95), (0, 95)], GREY),
        ('PARALLELOGRAM', [(30, 20), (150, 20), (120, 100), (0, 100)], PURP),
        ('RHOMBUS', [(60, 0), (120, 60), (60, 120), (0, 60)], GREEN),
        ('TRAPEZOID', [(35, 15), (105, 15), (140, 100), (0, 100)], '#9A6A3A'),
        ('HEXAGON', [(35, 5), (100, 5), (135, 60), (100, 115), (35, 115), (0, 60)], '#2F9E7A'),
    ]
    verbs = ['STRETCH', 'SHEAR', 'PUSH', 'CUT', 'ADD SIDES']
    x = 70
    for i, (name, pts, col) in enumerate(shapes):
        P = [(x + px, 270 + py) for (px, py) in pts]
        S.wash(P, col, .65); S.poly(P, w=1.8)
        S.text(x + 60, 430, name, size=16, anchor='middle')
        if i < len(verbs):
            S.arrow(x + 150, 330, x + 178, 330, w=1.3)
            S.text(x + 164, 310, verbs[i], size=12, anchor='middle', color='#B5432A')
        x += 180
    # touch path diagram
    S.text(70, 520, 'HOW A CHILD READS A SHAPE', size=22)
    bx, by = 90, 560
    sq = [(bx, by), (bx + 200, by), (bx + 200, by + 200), (bx, by + 200)]
    S.wash(sq, RED, .45); S.poly(sq, w=1.8)
    for (px, py) in sq:
        S.circle(px, py, 12, w=1.2)
    S.arrow(bx + 20, by - 18, bx + 180, by - 18, color='#B5432A'); S.arrow(bx + 218, by + 20, bx + 218, by + 180, color='#B5432A')
    S.text(bx + 100, by + 110, '4 CORNERS', size=17, anchor='middle')
    S.text(bx + 100, by + 132, '4 EQUAL SIDES', size=17, anchor='middle')
    S.leader(bx + 200, by, 420, 600, 'FIND THE CORNERS FIRST')
    S.leader(bx + 200, by + 100, 420, 660, 'TRACE EACH SIDE, COUNT')
    S.leader(bx + 100, by + 200, 420, 720, 'COMPARE WITH THE NEXT PAGE')
    # page thumbnails sketch
    for k, (col, lab) in enumerate([(PURP, 'FACE PAGE'), (YEL, 'BUBBLE TEXTURE'), (ORANGE, 'RATTLE DRUM'), (PINK, 'BUTTON TREE')]):
        x0 = 720 + (k % 2) * 220; y0 = 480 + (k // 2) * 150
        pg = [(x0, y0), (x0 + 190, y0), (x0 + 190, y0 + 110), (x0, y0 + 110)]
        S.wash(pg, col, .4); S.poly(pg, w=1.3)
        S.line(x0 + 95, y0, x0 + 95, y0 + 110, w=0.9)
        S.poly([(x0 + 110, y0 + 22), (x0 + 175, y0 + 22), (x0 + 175, y0 + 88), (x0 + 110, y0 + 88)], w=1)
        S.text(x0 + 95, y0 + 130, lab, size=13, anchor='middle')
    S.title_block('SEQUENCE — FANGFANG\'S TRANSFORMATIONS', 'EACH PAGE CHANGES ONE THING · TEXTURE, SOUND OR MOVEMENT ON EVERY SPREAD', 'A-04')
    S.save(path)


if __name__ == '__main__':
    import sys
    out = sys.argv[1]
    sheet1(out + '/arch1.png'); sheet2(out + '/arch2.png'); sheet3(out + '/arch3.png'); sheet4(out + '/arch4.png')
    print('done')
