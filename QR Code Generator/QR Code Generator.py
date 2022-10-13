# QR Code Generator
import pyqrcode
from pyqrcode import QRCode
# String which represent the QR code 
s = "https://sanjay-dutta.github.io/sanjay/"
# Generate QR code 
url = pyqrcode.create(s) 
# Create and save the png file naming "myqr.png" 
url.svg("mywebsite.svg", scale = 4) 