import cv2

file = 'main_menu/img/tetris.png'

img = cv2.imread(file, cv2.IMREAD_UNCHANGED)

for i in range(len(img)):
    for j in range(len(img[i])):
        if img[i][j][3] == 0:
            img[i][j] = [255,255,255, 255]

cv2.imwrite(file, img)