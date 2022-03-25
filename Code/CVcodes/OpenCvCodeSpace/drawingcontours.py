from multiprocessing.connection import wait
#using canny edge detection to detect contour

import cv2
from matplotlib.pyplot import contour
import numpy as np

image = cv2.imread("dribbler.jpg.jpg")
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh=cv2.threshold(gray, 127, 255, 0)

############## contours is a python list of all the contours in the image.##############

contours, hierachy =cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of Contours = " +str(len(contours)))
print(contours[0])

cv2.drawContours(image, contours, -1, (0,255,0), 3)

size1=cv2.resize(image, (480,480))
size=cv2.resize(gray, (480,480))

cv2.imshow("image1", size1)
cv2.imshow("image", size)


cv2.waitKey(0)
cv2.destroyAllWindows()