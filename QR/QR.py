import cv2
from pyzbar.pyzbar import decode
import qrcode

def MakeQR(text, name):
    '''
    QR 코드 만드는 코드
        입력 : 
            text (str) : QR코드 안에 들어갈 내용
            name (str) : 저장될 때 이름
    '''
    QR = qrcode.make(text)
    QR.save(str(name)+'.png')

def ReadQR(img):
    '''
    QR 코드 읽는 코드
        입력 :
            img (np.array) : QR 정보를 읽을 사진

        출력 :
            QR 코드의 내용 (없을시 None return)
    '''
    img = cv2.resize(img, (0,0),fx=0.3,fy=0.3)
    decoded = decode(img)
    for d in decoded:
        return d.data.decode('utf-8')

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()

    if status:
        cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

print(ReadQR(frame))