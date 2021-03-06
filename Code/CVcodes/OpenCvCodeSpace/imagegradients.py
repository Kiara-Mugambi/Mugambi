#image gradient is thee directional change in the intensity or color in an image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("dribbler.jpg.jpg")
lap=cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap=np.uint8(np.absolute(lap))
sobelX= cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY=cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

titles=["image", "Laplace", "SobelX", "SobelY"]
images=[img, lap, sobelX, sobelY]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()