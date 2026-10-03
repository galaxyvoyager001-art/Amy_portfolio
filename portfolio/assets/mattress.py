import math, cairosvg

W, H = 2000, 1250
C30, S30 = math.cos(math.radians(30)), math.sin(math.radians(30))
OX, OY, SC = 980, 330, 1.0


def iso(x, y, z):
    return (OX + (x - y) * C30 * SC, OY + (x + y) * S30 * SC - z * SC)


def poly(pts, fill, stroke='none', sw=0, op=1.0):
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    return f'<polygon points="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}" stroke-linejoin="round"/>'


def shade(hexc, f):
    h = hexc.lstrip('#'); r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    r, g, b = [max(0, min(255, int(v * f))) for v in (r, g, b)]
    return f'#{r:02x}{g:02x}{b:02x}'


out = []
# background
out.append('<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3F6FA"/><stop offset="1" stop-color="#DCE4EE"/></linearGradient>'
           '<radialGradient id="sh" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#1b2a44" stop-opacity=".28"/><stop offset="1" stop-color="#1b2a44" stop-opacity="0"/></radialGradient></defs>')
out.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')

NX, NY = 18, 20            # cells across (x) and along (y)
CW = 40                   # cell pitch
LX, LY = NX * CW, NY * CW  # 720 x 800
BASE = 70                 # base thickness

# floor shadow
cx, cy = iso(LX / 2, LY / 2, -BASE)
out.append(f'<ellipse cx="{cx:.0f}" cy="{cy + 40:.0f}" rx="760" ry="300" fill="url(#sh)"/>')

# frame / base block
z0 = 0
top = [iso(-14, -14, z0), iso(LX + 14, -14, z0), iso(LX + 14, LY + 14, z0), iso(-14, LY + 14, z0)]
bot = [iso(-14, -14, z0 - BASE), iso(LX + 14, -14, z0 - BASE), iso(LX + 14, LY + 14, z0 - BASE), iso(-14, LY + 14, z0 - BASE)]
out.append(poly([top[1], top[2], bot[2], bot[1]], '#B9C3CF'))   # right side (x = max)
out.append(poly([top[2], top[3], bot[3], bot[2]], '#D3DAE3'))   # front side (y = max)
out.append(poly(top, '#E8EDF3'))
# piping groove + label strip on front
a, b = iso(-14, LY + 14, z0 - 30), iso(LX + 14, LY + 14, z0 - 30)
out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#AEB8C4" stroke-width="3"/>')

# cells with a travelling wave; cut-away corner (front-left) shows the layers
CUT_X, CUT_Y = 6, 6   # cells removed at x < CUT_X and y >= NY - CUT_Y
cells = []
for i in range(NX):
    for j in range(NY):
        if i < CUT_X and j >= NY - CUT_Y:
            continue
        phase = (j / NY) * 2 * math.pi * 1.6
        h = 24 + 26 * (0.5 + 0.5 * math.sin(phase - 1.2))
        tilt = 16 * math.cos(phase - 1.2)
        cells.append((i, j, h, tilt))
cells.sort(key=lambda c: (c[0] + c[1]))
for i, j, h, tilt in cells:
    x0, y0 = i * CW + 3, j * CW + 3
    x1, y1 = x0 + CW - 6, y0 + CW - 6
    zt0, zt1 = h + tilt * 0.4, h - tilt * 0.4   # slanted top = deflection of the unit
    t = [iso(x0, y0, zt0), iso(x1, y0, zt0), iso(x1, y1, zt1), iso(x0, y1, zt1)]
    bb = [iso(x0, y0, 0), iso(x1, y0, 0), iso(x1, y1, 0), iso(x0, y1, 0)]
    lum = 0.90 + 0.10 * (h - 24) / 26
    out.append(poly([t[1], t[2], bb[2], bb[1]], shade('#CFE3EC', lum * 0.86)))
    out.append(poly([t[2], t[3], bb[3], bb[2]], shade('#CFE3EC', lum * 0.95)))
    out.append(poly(t, shade('#EEF7FB', lum), '#C3D5DF', 0.8))

# bed sheet, folded back to show the cells
SY = LY * 0.30
SH = 66
sheet = [iso(-6, -6, SH), iso(LX + 6, -6, SH), iso(LX + 6, SY, SH), iso(-6, SY, SH)]
out.append(poly(sheet, '#FFFFFF', '#9FB3C3', 1.2, op=0.9))
fold = [iso(-6, SY, SH), iso(LX + 6, SY, SH), iso(LX + 6, SY + 26, SH - 6), iso(-6, SY + 26, SH - 6)]
out.append(poly(fold, '#E6EEF4', '#9FB3C3', 1.0, op=0.95))
for k in range(1, 5):
    yy = k * SY / 5
    a_, b_ = iso(-6, yy, SH + 1), iso(LX + 6, yy, SH + 1)
    out.append(f'<line x1="{a_[0]:.1f}" y1="{a_[1]:.1f}" x2="{b_[0]:.1f}" y2="{b_[1]:.1f}" stroke="#C9D7E2" stroke-width="1.4" stroke-dasharray="7 6"/>')

# cut-away layer edges (exploded steps in the corner)
def slab(xa, ya, xb, yb, z, th, col):
    t = [iso(xa, ya, z), iso(xb, ya, z), iso(xb, yb, z), iso(xa, yb, z)]
    b = [iso(xa, ya, z - th), iso(xb, ya, z - th), iso(xb, yb, z - th), iso(xa, yb, z - th)]
    return [poly([t[1], t[2], b[2], b[1]], shade(col, .82)), poly([t[2], t[3], b[3], b[2]], shade(col, .92)), poly(t, col, shade(col, .7), 1)]

ya = (NY - CUT_Y) * CW
for part in slab(0, ya, CUT_X * CW - 120, LY, 8, 8, '#8E9AA8'):          # silicone base
    out.append(part)
for part in slab(0, ya, CUT_X * CW - 170, LY - 50, 22, 10, '#F1D27A'):    # confining layer (cotton)
    out.append(part)
for part in slab(0, ya, CUT_X * CW - 220, LY - 100, 38, 8, '#7FC7C0'):    # coating / sheet
    out.append(part)
# two exposed demo cells in the cut-away, one inflated
for k, (cx_, cy_, hh, tl) in enumerate([(CUT_X * CW - 80, LY - 60, 30, 0), (CUT_X * CW - 40, LY - 140, 44, 14)]):
    x0, y0, x1, y1 = cx_, cy_, cx_ + 34, cy_ + 34
    t = [iso(x0, y0, hh + tl), iso(x1, y0, hh + tl), iso(x1, y1, hh - tl), iso(x0, y1, hh - tl)]
    bb = [iso(x0, y0, 0), iso(x1, y0, 0), iso(x1, y1, 0), iso(x0, y1, 0)]
    out.append(poly([t[1], t[2], bb[2], bb[1]], '#BFD9E4')); out.append(poly([t[2], t[3], bb[3], bb[2]], '#D6EAF1')); out.append(poly(t, '#F2FAFD', '#9DB8C6', 1))

# control unit with pump and valve manifold, tubes into the base
ux, uy = 1640, 760
out.append(f'<rect x="{ux}" y="{uy}" width="230" height="170" rx="18" fill="#2E3A59"/>')
out.append(f'<rect x="{ux + 14}" y="{uy + 14}" width="202" height="60" rx="8" fill="#0F172A"/>')
out.append(f'<text x="{ux + 115}" y="{uy + 52}" font-family="DejaVu Sans" font-size="22" fill="#7FE0D6" text-anchor="middle">WAVE · 04</text>')
for k in range(4):
    out.append(f'<circle cx="{ux + 40 + k * 50}" cy="{uy + 120}" r="15" fill="{["#7FC7C0", "#F1D27A", "#7FC7C0", "#F1D27A"][k]}"/>')
pt = iso(LX + 14, LY - 40, -30)
for k in range(4):
    out.append(f'<path d="M{ux} {uy + 100 + k * 12} C {ux - 160} {uy + 120 + k * 12}, {pt[0] + 140} {pt[1] + 10 + k * 8}, {pt[0] + 4} {pt[1] + k * 8}" fill="none" stroke="#5E6B80" stroke-width="5" stroke-linecap="round"/>')

# wave arrow over the top
p1, p2 = iso(LX * 0.55, 30, 150), iso(LX * 0.55, LY - 60, 150)
out.append(f'<path d="M{p1[0]:.0f} {p1[1]:.0f} Q {(p1[0] + p2[0]) / 2 + 60:.0f} {(p1[1] + p2[1]) / 2 - 80:.0f} {p2[0]:.0f} {p2[1]:.0f}" fill="none" stroke="#E8552B" stroke-width="6" stroke-dasharray="18 12"/>')
out.append(f'<polygon points="{p2[0]:.0f},{p2[1]:.0f} {p2[0] - 30:.0f},{p2[1] - 4:.0f} {p2[0] - 12:.0f},{p2[1] - 28:.0f}" fill="#E8552B"/>')

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">' + ''.join(out) + '</svg>'
cairosvg.svg2png(bytestring=svg.encode(), write_to='mattress.png', output_width=W, output_height=H)
print('ok')
