import cv2 as cv

img = cv.imread('Tank/tank.png', cv.IMREAD_UNCHANGED)
print(img.shape)

'''
for i in range(img.shape[1]):
    count = 0
    for j in range(img.shape[0]):
        if img[j][i][3] == 255:
            count += 1
    print('%d줄 %d개'%(i,count))
'''

'''
cut=[[8,88],[140,256],[272,365],[403,511],[535,609],[668,772],[800,913],[932,1043]]

for i in range(len(cut)):
    cv.imwrite(str(i+1)+'_Tank.png', img[:,cut[i][0]:cut[i][1],:])
'''

'''
for i in range(8):
    img = cv.imread('Tank/'+str(i+1)+'_Tank.png', cv.IMREAD_UNCHANGED)
    for j in range(img.shape[0]):
        count = 0
        for z in range(img.shape[1]):
            if img[j][z][3] == 255:
                count+=1
        print('%d번이미지 %d줄 %d개'%(i+1,j,count))

    print('=============================')
'''

'''
cut = [[8,200],[8,246],[8,262],[8,233],[8,171],[8,282],[8,245],[8,235]]

for i in range(8):
    img = cv.imread('Tank/'+str(i+1)+'_Tank.png', cv.IMREAD_UNCHANGED)
    cv.imwrite(str(i+1)+'_Tank.png', img[cut[i][0]:cut[i][1],:,:])
'''