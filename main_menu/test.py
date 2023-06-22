import cv2

file = 'main_menu\img\joystick.png'

img = cv2.imread(file)

for i in range(len(img)):
    for j in range(len(img[i])):
        if img[i][j][0].sum() == 0:
            img[i][j] = [255,255,255]

cv2.imwrite(file, img)