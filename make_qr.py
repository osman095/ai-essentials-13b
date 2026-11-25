import sys
import qrcode

# usage: python make_qr.py [text] [output file]
text = sys.argv[1] if len(sys.argv) > 1 else "Happy Diwali"
out = sys.argv[2] if len(sys.argv) > 2 else "qr.png"

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(out)
print("saved", out, "size", img.size)
