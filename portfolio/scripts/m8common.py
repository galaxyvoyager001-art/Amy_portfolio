"""Research pages 16, 17, 19, 20: page-15 style, four different layouts."""
import math, re
P = '/home/user/Amy_portfolio/portfolio/project/'
SRC = open(P + 'Mind-IYPT.dc.html').read()
HEAD = SRC[:SRC.index('</style>')]
INK, PAPER = '#1A1A1A', '#F6F2EA'
EXTRA = """.ef img.cap{max-height:230px;width:auto;max-width:100%;margin:0 auto}
.tbl{width:100%;border-collapse:collapse;font-family:'Instrument Sans',sans-serif;font-size:10px}
.tbl th,.tbl td{padding:3px 4px;border-bottom:1px solid #D9D2C3;text-align:right}
.tbl th:first-child,.tbl td:first-child{text-align:left}
.tbl tr.hi td{font-weight:700}
.wcol{font-family:'Source Serif 4',Georgia,serif;font-size:13px;line-height:1.48;text-align:justify;hyphens:auto;-webkit-hyphens:auto;column-gap:26px;color:#FFFFFF}
.wcol p{margin:0 0 9px}
.lbl{font-family:'Instrument Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}
.card{background:#FFFFFF;padding:8px 8px 6px}
"""
TAIL = """</style>
</helmet>
<div style="width: 1920px; height: 960px; position: relative; overflow: hidden; background: {bg}">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1920,"height":960}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""


def write(fname, title, bg, body):
    head = HEAD[:HEAD.index('<title>')] + f'<title>{title}</title>' + HEAD[HEAD.index('</title>') + 8:]
    open(P + fname, 'w').write(head + EXTRA + TAIL.format(bg=bg, body=body))


def fig(bid, alt, cap, cls='', style=''):
    return f'<figure class="ef"><img class="{cls}" src="/_blob/{bid}" alt="{alt}" style="{style}"><figcaption class="fcap">{cap}</figcaption></figure>'


def figh(inner, cap):
    return f'<figure class="ef">{inner}<figcaption class="fcap">{cap}</figcaption></figure>'


def kws(items, x, w, y, col=INK, top=None):
    pos = f'top: {top}px' if top is not None else f'bottom: {y}px'
    out = f'<div style="position: absolute; left: {x}px; width: {w}px; {pos}; display: grid; grid-template-columns: repeat({len(items)}, minmax(0, 1fr)); gap: 22px; color: {col}">\n'
    for n, t in items:
        out += f'<div class="kw"><b>{n}</b><span>{t}</span></div>\n'
    return out + '</div>\n'


def secs(acc, items):
    return ''.join(f'<h5 style="color: {acc}">{h}</h5>{b}' for h, b in items)

