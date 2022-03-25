#pyramid representation is the type of multi-scale signal representation that signal or an image is subject to repeated smoothing and subsampling
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("argentina.jpg", 1)
image=cv2.resize(img, (480,480))
layer=img.copy()
gp=[layer]

'''lr= cv2.pyrDown(image)
lr1=cv2.pyrDown(lr)

cv2.imshow("image", image)
cv2.imshow("lr", lr)
cv2.imshow("lr1", lr1)
'''
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer=gp[5]
cv2.imshow("upper level Gaussian Pyramid", layer)
lp= [layer]

for i in range(5, 0, -1):
    gaussian_extended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()