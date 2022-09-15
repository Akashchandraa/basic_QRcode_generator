import pyqrcode
import png
from pyqrcode import QRCode

a = "https://github.com/Akashchandraa/basic_turtle_project.git"

crt = pyqrcode.create(a)
crt.svg("myqr.svg", scale=10)
crt.png("myqr.png", scale=8)
