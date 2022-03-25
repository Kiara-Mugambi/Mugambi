from cv2 import MORPH_GRADIENT
import numpy as np
import matplotlib as plt
import cv2

image=cv2.imread("forerosion.PNG")
kernel=np.ones((5,5), np.uint8)
dilate=cv2.dilate(image, kernel, iterations=1)
Gradient=cv2.morphologyEx(image, MORPH_GRADIENT,kernel)

cv2.imshow("Image", image)
cv2.imshow("Dilation", dilate)
cv2.imshow("Gradient", Gradient)

cv2.waitKey(0)
cv2.destroyAllWindows