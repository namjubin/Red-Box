import qrcode

text = 'T-rex_run'
QR = qrcode.make(text)
QR.save(text+'.png')