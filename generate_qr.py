import qrcode as qr 
img= qr.make("https://www.youtube.com/@freecodecamp")
img.save("FreeCodeCamp_Youtube.png")