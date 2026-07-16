import html, sys

portrait = open(sys.argv[1]).read().rstrip("\n").split("\n")

BG      = "#11151c"
BORDER  = "#2d333b"
BAR     = "#1a2028"
PURPLE  = "#b794f4"
BLUE    = "#58a6ff"
KEY     = "#79c0ff"
VAL     = "#c9d1d9"
DIM     = "#8b949e"
GREEN   = "#7ee787"
ORANGE  = "#ffa657"

FS, LH = 12, 15                 # info text
FS_ART, LH_ART = 8, 8.6         # portrait: smaller font, tight leading
CW = FS * 0.65
CW_ART = FS_ART * 0.65

K, V = 0, 13
def kv(k, v, vcolor=VAL): return [(K, k, KEY), (V, v, vcolor)]
def sec(t): return [(0, t, GREEN)]
DIVIDER = "DIVIDER"

info = [
    [(0, "Y Thananjhayan", BLUE), (15, "· YThana", DIM)],
    DIVIDER,
    kv("Role", "Full-stack Developer · 3+ yrs"),
    kv("Base", "Batticaloa, Sri Lanka"),
    kv("Edu", "MSc CS (reading) · BSc ICT — USJ"),
    [],
    sec("~/work"),
    kv("Gravitide", "Full-stack Dev · 2025 — now", ORANGE),
    [(V, "Nuxt · Hono · FastAPI · Supabase", DIM)],
    kv("Trivyol", "Front-end Dev · 2023 — now", ORANGE),
    [(V, "Industrial SCADA front-ends · Dashboards", DIM)],
    [(V, "Maps · AI chat · FastAPI", DIM)],
    [],
    sec("~/stack"),
    kv("Lang", "TypeScript · JavaScript · Python · C"),
    kv("Frontend", "Vue · Nuxt · React · Tailwind"),
    kv("Backend", "Node.js · FastAPI · Hono"),
    kv("Data", "PostgreSQL · MySQL · Supabase · Firebase"),
    kv("Tools", "Docker · Git & GitHub"),
    [],
    sec("~/speak"),
    [(0, "Tamil", VAL), (6, "native", DIM), (14, "· English", VAL), (24, "fluent", DIM), (31, "· Sinhala", VAL), (41, "basic", DIM)],
    [],
    sec("~/reach"),
    kv("Web", "ythananjhayan.com"),
    kv("LinkedIn", "linkedin.com/in/thananjhayan-yohenthiran"),
    kv("GitHub", "github.com/YThana"),
    kv("Mail", "ythana09@gmail.com"),
]

info_chars = max((col + len(text)) for row in info if row and row != DIVIDER for col, text, _ in row)

PAD_X, PAD_TOP = 28, 64
ART_W = max(len(l) for l in portrait) * CW_ART
ART_H = len(portrait) * LH_ART
INFO_H = len(info) * LH
INFO_X = PAD_X + ART_W + 36
INFO_W = info_chars * CW
W = int(INFO_X + INFO_W + PAD_X)

y0 = PAD_TOP            # prompt line
art_y = y0 + LH * 1.6
info_y = art_y + max(0, (ART_H - INFO_H) / 2)
body_bottom = art_y + max(ART_H, INFO_H)
fy = body_bottom + LH * 1.4
H = int(fy + 26)

def esc(s): return html.escape(s, quote=False)

out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="{FS}">')
out.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="{BG}" stroke="{BORDER}"/>')
out.append(f'<rect x="1" y="1" width="{W-2}" height="34" rx="12" fill="{BAR}"/><rect x="1" y="24" width="{W-2}" height="12" fill="{BAR}"/>')
out.append(f'<circle cx="24" cy="18" r="5.5" fill="#ff5f57"/><circle cx="44" cy="18" r="5.5" fill="#febc2e"/><circle cx="64" cy="18" r="5.5" fill="#28c840"/>')
out.append(f'<text x="{W/2}" y="22" text-anchor="middle" fill="{DIM}">YThana — zsh</text>')

out.append(f'<text x="{PAD_X}" y="{y0}"><tspan fill="{GREEN}">➜</tspan><tspan fill="{BLUE}"> ~ </tspan><tspan fill="{VAL}">neofetch --profile</tspan></text>')

for i, line in enumerate(portrait):
    if line.strip():
        out.append(f'<text x="{PAD_X}" y="{art_y + i*LH_ART:.1f}" xml:space="preserve" fill="{PURPLE}" font-size="{FS_ART}" textLength="{len(line)*CW_ART:.1f}" lengthAdjust="spacingAndGlyphs">{esc(line)}</text>')

for i, row in enumerate(info):
    if not row: continue
    yy = info_y + i * LH
    if row == DIVIDER:
        out.append(f'<line x1="{INFO_X}" y1="{yy-4:.1f}" x2="{INFO_X + INFO_W:.0f}" y2="{yy-4:.1f}" stroke="{BORDER}"/>')
        continue
    spans = "".join(f'<tspan x="{INFO_X + col*CW:.1f}" fill="{color}" textLength="{len(text)*CW:.1f}" lengthAdjust="spacingAndGlyphs">{esc(text)}</tspan>' for col, text, color in row)
    out.append(f'<text y="{yy:.1f}" xml:space="preserve">{spans}</text>')

out.append(f'<text x="{PAD_X}" y="{fy:.1f}"><tspan fill="{GREEN}">➜</tspan><tspan fill="{BLUE}"> ~ </tspan><tspan fill="{VAL}">building with Vue, Nuxt, Hono.js, FastAPI &amp; AI</tspan><tspan fill="{DIM}"> ▍</tspan></text>')
out.append('</svg>')

open(sys.argv[2], "w").write("\n".join(out))
print(f"wrote {sys.argv[2]} ({W}x{H})")
