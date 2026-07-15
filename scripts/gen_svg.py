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

FS = 12
LH = 15
CW = FS * 0.65   # generous monospace char width so nothing clips

K, V = 0, 13
def kv(k, v, vcolor=VAL): return [(K, k, KEY), (V, v, vcolor)]
def sec(t): return [(0, t, GREEN)]
DIVIDER = "DIVIDER"

info = [
    [(0, "thana", BLUE), (6, "· YThana", DIM)],
    DIVIDER,
    kv("Role", "Full-stack Developer"),
    kv("Base", "Batticaloa, Sri Lanka"),
    kv("Focus", "Full-stack Web · AI-powered Apps"),
    [],
    sec("~/stack"),
    kv("Lang", "TypeScript · JavaScript · Python · SQL"),
    kv("Frontend", "Vue · Nuxt · Ionic"),
    kv("Backend", "Node.js · Nitro · FastAPI"),
    kv("AI", "Vercel AI SDK · Gemini"),
    kv("Data", "PostgreSQL (Neon) · Drizzle ORM"),
    [],
    sec("~/projects"),
    kv("wa-bot", "AI commerce bot on WhatsApp", ORANGE),
    [(V, "Meta Cloud API · Nuxt 4 · Gemini", DIM)],
    kv("myseedbox", "Self-hosted seedbox", ORANGE),
    [(V, "Vue · FastAPI · qBittorrent", DIM)],
    kv("smart-stock", "Inventory management · Nuxt", ORANGE),
    [],
    sec("~/reach"),
    kv("GitHub", "github.com/YThana"),
    kv("Mail", "ythana09@gmail.com"),
]

info_chars = max((col + len(text)) for row in info if row and row != DIVIDER for col, text, _ in row)

PAD_X, PAD_TOP = 28, 64
ART_W = max(len(l) for l in portrait) * CW
INFO_X = PAD_X + ART_W + 36
INFO_W = info_chars * CW
W = int(INFO_X + INFO_W + PAD_X)
body_lines = max(len(portrait) + 2, len(info) + 2)
H = int(PAD_TOP + (body_lines + 1) * LH + 26)

def esc(s): return html.escape(s, quote=False)

out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="{FS}">')
out.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="{BG}" stroke="{BORDER}"/>')
out.append(f'<rect x="1" y="1" width="{W-2}" height="34" rx="12" fill="{BAR}"/><rect x="1" y="24" width="{W-2}" height="12" fill="{BAR}"/>')
out.append(f'<circle cx="24" cy="18" r="5.5" fill="#ff5f57"/><circle cx="44" cy="18" r="5.5" fill="#febc2e"/><circle cx="64" cy="18" r="5.5" fill="#28c840"/>')
out.append(f'<text x="{W/2}" y="22" text-anchor="middle" fill="{DIM}">YThana — zsh</text>')

y = PAD_TOP
out.append(f'<text x="{PAD_X}" y="{y}"><tspan fill="{GREEN}">➜</tspan><tspan fill="{BLUE}"> ~ </tspan><tspan fill="{VAL}">neofetch --profile</tspan></text>')

art_y = y + LH * 2
for i, line in enumerate(portrait):
    if line.strip():
        out.append(f'<text x="{PAD_X}" y="{art_y + i*LH}" xml:space="preserve" fill="{PURPLE}" textLength="{len(line)*CW:.1f}" lengthAdjust="spacingAndGlyphs">{esc(line)}</text>')

for i, row in enumerate(info):
    if not row: continue
    yy = art_y + i * LH
    if row == DIVIDER:
        out.append(f'<line x1="{INFO_X}" y1="{yy-4}" x2="{INFO_X + INFO_W:.0f}" y2="{yy-4}" stroke="{BORDER}"/>')
        continue
    spans = "".join(f'<tspan x="{INFO_X + col*CW:.1f}" fill="{color}" textLength="{len(text)*CW:.1f}" lengthAdjust="spacingAndGlyphs">{esc(text)}</tspan>' for col, text, color in row)
    out.append(f'<text y="{yy}" xml:space="preserve">{spans}</text>')

fy = art_y + (body_lines - 1) * LH
out.append(f'<text x="{PAD_X}" y="{fy}"><tspan fill="{GREEN}">➜</tspan><tspan fill="{BLUE}"> ~ </tspan><tspan fill="{VAL}">building with Vue, Nuxt &amp; AI</tspan><tspan fill="{DIM}"> ▍</tspan></text>')
out.append('</svg>')

open(sys.argv[2], "w").write("\n".join(out))
print(f"wrote {sys.argv[2]} ({W}x{H})")
