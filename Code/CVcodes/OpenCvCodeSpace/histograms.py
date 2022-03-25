import numpy as np
from matplotlib import pyplot as plt
import cv2

image=cv2.imread("argentina.jpg")
imagescaled=cv2.resize(image, (480,480))

b, g, r =cv2.split(imagescaled)
hist=cv2.calcHist([imagescaled], [0], None, [256], [0, 256] )
plt.plot(hist)

#image=np.zeros((200,200), np.uint8)
#cv2.rectangle(image, (0,100), (200,200), (255), -1)

'''cv2.imshow("Image", imagescaled )
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)

#plt.hist(imagescaled.ravel(), 256, [0, 256])
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0,256])
'''
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()