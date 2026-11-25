import sys
from pyfiglet import Figlet

# usage: python banner.py [text] [font]
text = sys.argv[1] if len(sys.argv) > 1 else "Diwali"
font = sys.argv[2] if len(sys.argv) > 2 else "big"

print(Figlet(font=font).renderText(text))
