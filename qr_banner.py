import sys
import qrcode
from pyfiglet import Figlet
from PIL import Image, ImageDraw, ImageFont

# usage: python qr_banner.py [qr text] [caption] [output file]
qr_text = sys.argv[1] if len(sys.argv) > 1 else "Happy Diwali"
caption = sys.argv[2] if len(sys.argv) > 2 else "Diwali"
out = sys.argv[3] if len(sys.argv) > 3 else "qr_banner.png"

# 1. QR code image (qrcode)
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(qr_text)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# 2. banner text (pyfiglet)
banner = Figlet(font="big").renderText(caption).rstrip("\n")
lines = banner.split("\n")

# 3. draw the banner under the QR code (Pillow)
try:
    font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 16)
except OSError:
    font = ImageFont.load_default()

ascent, descent = font.getmetrics()
char_w = font.getlength("M")
line_h = ascent + descent
text_w = int(char_w * max(len(l) for l in lines))
text_h = line_h * len(lines)

width = max(qr_img.width, text_w + 40)
height = qr_img.height + text_h + 30
canvas = Image.new("RGB", (width, height), "white")
canvas.paste(qr_img, ((width - qr_img.width) // 2, 0))

draw = ImageDraw.Draw(canvas)
x = (width - text_w) // 2
y = qr_img.height + 10
for line in lines:
    draw.text((x, y), line, font=font, fill="black")
    y += line_h

canvas.save(out)
print("saved", out, "size", canvas.size)
