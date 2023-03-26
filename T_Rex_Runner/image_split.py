import cv2 as cv
import numpy as np

img = cv.imread('T_Rex_Runner\T-Rex_image\cacti-big.png', cv.IMREAD_UNCHANGED)
print(img.shape)

for i in range(0, img.shape[1], 50):
    cv.imwrite(str(i)+'.png',img[:,i:i+50])
    