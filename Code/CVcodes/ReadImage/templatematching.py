from matplotlib import pyplot as plt
import numpy as np
import cv2
import pytesseract

image=cv2.imread("dribbler.jpg")
#image1=cv2.resize(image, (480,480))
greyscaleimage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template=cv2.imread("messitemplate.jpg", 0)

w,h =template.shape[:: -1]

res=cv2.matchTemplate(greyscaleimage, template, cv2.TM_CCOEFF_NORMED)
print(res)

threshold=0.8;

value=np.where(res >= threshold)
for pt in zip(*value[:: -1]):
    cv2.rectangle(image, pt, (pt[0] +w, pt[1] +h), (0,255,0), 2)
    
print(value)
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()