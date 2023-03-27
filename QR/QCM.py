import qrcode

text = 'tetris'
QR = qrcode.make(text)
QR.save(text+'.png')