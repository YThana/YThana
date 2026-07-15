from PIL import Image, ImageEnhance
import sys

W = int(sys.argv[2]) if len(sys.argv) > 2 else 62
img = Image.open(sys.argv[1]).convert("RGBA")
# composite over black, use alpha to blank background
bg = Image.new("RGBA", img.size, (0, 0, 0, 255))
img = Image.alpha_composite(bg, img)
alpha = Image.open(sys.argv[1]).convert("RGBA").getchannel("A")
gray = img.convert("L")
gray = ImageEnhance.Contrast(gray).enhance(1.3)
w, h = gray.size
H = int(h / w * W * 0.5)
gray = gray.resize((W, H))
alpha = alpha.resize((W, H))
chars = " .`':,;-~+=*!?#%@"
gp, ap = gray.load(), alpha.load()
lines = []
for y in range(H):
    row = ""
    for x in range(W):
        if ap[x, y] < 40:
            row += " "
        else:
            v = gp[x, y]
            v = max(v, 50)  # subject pixels never fully vanish
            row += chars[min(v * len(chars) // 256, len(chars) - 1)]
    lines.append(row.rstrip())
# trim empty top/bottom lines
while lines and not lines[0]: lines.pop(0)
while lines and not lines[-1]: lines.pop()
print("\n".join(lines))
