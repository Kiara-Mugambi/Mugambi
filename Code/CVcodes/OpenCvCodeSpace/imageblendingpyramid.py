import cv2
from cv2 import Laplacian
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("argentina.jpg")
img2=cv2.imread("dribbler.jpg.jpg")
argentina=cv2.resize(img, (480,480))
dribbler=cv2.resize(img2, (480,480))

print(argentina.shape)
print(dribbler.shape)

argentina_dribbler=np.hstack((argentina[:, :240], dribbler[:, 210:]))

#generating the Gaussian pyramid for argentina
argentina_copy=argentina.copy()
gp_argentina=[argentina_copy]

for i in range(6):
    argentina_copy=cv2.pyrDown(argentina_copy)
    gp_argentina.append(argentina_copy)

#generating the Gaussian pyramid for dribbler
dribbler_copy=dribbler.copy()
gp_dribbler=[dribbler_copy]

for i in range(6):
    dribbler_copy=cv2.pyrDown(dribbler_copy)
    gp_dribbler.append(dribbler_copy)

#generating laplacian pyramid for argentina
argentina_copy=gp_argentina[5]
lp_argentina=[argentina_copy]
for i in range(5, 0, -1):
    gaussian_expanded=cv2.pyrUp(gp_argentina[i])
    laplacian=cv2.subtract(gp_argentina[i-1], gaussian_expanded)
    lp_argentina.append(laplacian)

#generating laplacian pyramid for dribbler
dribbler_copy=gp_dribbler[5]
lp_dribbler=[dribbler_copy]
for i in range(5, 0, -1):
    gaussian_expanded=cv2.pyrUp(gp_dribbler[i])
    laplacian=cv2.subtract(gp_dribbler[i-1], gaussian_expanded)
    lp_dribbler.append(laplacian)

#add left and right halves of the two images
argentina_dribbler_pyramid=[]
n=0

for argentina_lap, dribbler_lap in zip(lp_dribbler, lp_argentina):
    n=+1
    cols, rows, ch =argentina_lap.shape
    laplacian=np.hstack((argentina_lap[:, 0:int(cols/2)], dribbler_lap[:, int(cols/2):]))
    argentina_dribbler_pyramid.append(laplacian)

#reconstruction
argentina_dribbler_reconstruct= argentina_dribbler_pyramid[0]
for i in range(1,6):
    argentina_dribbler_reconstruct=cv2.pyrUp(argentina_dribbler_reconstruct)
    argentina_dribbler_reconstruct=cv2.add(argentina_dribbler_pyramid[i], argentina_dribbler_reconstruct)

cv2.imshow("argentina_dribbler_reconstruct", argentina_dribbler_reconstruct)

cv2.imshow("IMAGE1", argentina)
cv2.imshow("IMAGE2", dribbler)
cv2.imshow("argentina_dribbler", argentina_dribbler)

cv2.waitKey(0)
cv2.destroyAllWindows()

