'''Optical Character Recognition:- OCR transforms a two dimensional image of text, that could contain machine printed
or handwritten text from its image representation into machine readable text.
Usually OCR as a process generally consists of several subprocesses to perform as accurately as possible.
The Subprocesses are;
1. Preprocessing of the Image
2. Text Localization
3. Character Segmentation
4. Character Recognition
5. Post Processing
'''
import numpy as np
from matplotlib import pyplot as plt
import cv2

image = cv2.imread("tesseract.jpg")
img=cv2.resize(image,(480,480))
grayscaleimage=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh, _=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)
kernel=np.ones((5,5), np.uint8)
dilation=cv2.dilate(img, kernel, iterations=3)
erosion=cv2.erode(img, kernel, iterations=1)
morphology=cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
canny=cv2.Canny(img, 100,200)

def deskew(img):
    coords = np.column_stack(np.where(img > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(img, template):
    return cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED) 

#titles=["Image","Grayscaleimage","Thresh", "Dilation", "Erosion", "Morphology", "Canny", "Kernel"]
#images=[image,grayscaleimage, thresh, dilation, erosion, morphology, canny, kernel]

'''for i in range(8):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])'''

#plt.show()
cv2.imshow("Image", img)
cv2.imshow("GrayScaleImage", grayscaleimage)
cv2.imshow("Opening", morphology)
cv2.imshow("Canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()