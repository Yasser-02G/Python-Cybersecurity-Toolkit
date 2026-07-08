import qrcode
img = qrcode.make("https://www.instagram.com/yasser_02_/")

img.show()
img.save("QR.png")