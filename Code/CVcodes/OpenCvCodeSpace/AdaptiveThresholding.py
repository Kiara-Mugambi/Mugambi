import cv2
from cv2 import ADAPTIVE_THRESH_MEAN_C
 

image=cv2.imread("argentina.jpg",0)
#gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image1=cv2.resize(image, (480,480))

#thresh=cv2.threshold(image, 70, 255, cv2.THRESH_BINARY)
adapt=cv2.adaptiveThreshold(image, 255, ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

#cv2.namedWindow("thresh", cv2.WINDOW_NORMAL)
cv2.namedWindow("adapt", cv2.WINDOW_NORMAL)

#cv2.imshow("thresh", thresh)
cv2.imshow("adapt", adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()