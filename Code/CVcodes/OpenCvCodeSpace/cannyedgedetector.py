#canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images
#Gaussian filter is applied to reduce noisein surrounding
#canny edge detector applies gradient intensity
#non-maximum suppression
#double threshold
#edge tracking by hysteresis

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("dribbler.jpg.jpg")
canny=cv2.Canny(img, 100, 200)

titles=["Images", "Canny"]
images=[img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], )
    plt.title(titles[i])

plt.show()