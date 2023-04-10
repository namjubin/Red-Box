import qrcode

text = ''
QR = qrcode.make(text)
QR.save(text+'.png')