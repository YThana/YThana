from PIL import Image, ImageEnhance, ImageOps
import sys

src = sys.argv[1]
W = int(sys.argv[2]) if len(sys.argv) > 2 else 96
GAMMA = float(sys.argv[3]) if len(sys.argv) > 3 else 0.60

rgba = Image.open(src).convert("RGBA")
bg = Image.new("RGBA", rgba.size, (0, 0, 0, 255))
flat = Image.alpha_composite(bg, rgba)
alpha = rgba.getchannel("A")
gray = flat.convert("L")
gray = ImageEnhance.Contrast(gray).enhance(1.2)

w, h = gray.size
H = int(h / w * W * 0.5)
gray_s = gray.resize((W, H))
alpha_s = alpha.resize((W, H))

chars = " .`':,;-~+=*!?#%@"
n = len(chars)
gp, ap = gray_s.load(), alpha_s.load()
lines = []
for y in range(H):
    row = ""
    for x in range(W):
        if ap[x, y] < 40:
            row += " "
            continue
        # gamma-lift shadows so dark hair stays visible; keep facial contrast
        v = 255 * (gp[x, y] / 255) ** GAMMA
        v = max(v, 40)
        row += chars[min(int(v) * n // 256, n - 1)]
    lines.append(row.rstrip())
while lines and not lines[0]: lines.pop(0)
while lines and not lines[-1]: lines.pop()
print("\n".join(lines))
