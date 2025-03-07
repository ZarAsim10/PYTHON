import qrcode 
img = qrcode.make("https://www.linkedin.com/in/zara-salah-674177289")
print(type(img))
img.save ("Zara LinkedIn.png")
print('QR code has been generated successfully')