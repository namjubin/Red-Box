import cv2 as cv
import numpy as np

'''
for i in range(3):
    img = cv.imread('T_Rex_Runner\T-Rex_image\cacti_small_'+str(i+1)+'.png', cv.IMREAD_UNCHANGED)
    for y in range(len(img)):
        for x in range(len(img[y])):
            if img[y,x,3] != 0:
                if img[y,x,0] >= 200:
                    img[y,x]=[247,247,247,255]
                else:
                    img[y,x]=[83,83,83,255]
            else:
                img[y,x]=[0,0,0,0]

    cv.imwrite('T_Rex_Runner\T-Rex_image\cacti_small_'+str(i+1)+'.png',img)
'''

img = cv.imread('T_Rex_Runner/T-Rex_image/replay_button.png', cv.IMREAD_UNCHANGED)
for y in range(len(img)):
    for x in range(len(img[y])):
        if img[y,x,3] != 0:
            if img[y,x,0] >= 200:
                img[y,x]=[247,247,247,255]
            else:
                img[y,x]=[83,83,83,255]
        else:
            img[y,x]=[0,0,0,0]

cv.imwrite('T_Rex_Runner/T-Rex_image/replay_button.png',img)