import numpy as np
import matplotlib as plt
import cv2

image=cv2.imread("forerosion.PNG")
kernel=np.ones((8,8), np.uint8)
erode=cv2.erode(image, kernel, iterations=1)

cv2.imshow("erosion", erode)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()