import cv2
from matplotlib import pyplot as plt

image=cv2.imread("dribbler.jpg.jpg", 1)
image1= cv2.resize(image, (480,480))

cv2.imshow("Image", image1)
plt.imshow(image1)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()