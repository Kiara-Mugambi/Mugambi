import cv2
import pytesseract
from pytesseract import Output

image1=cv2.imread("Invoice.PNG")

'''h, w, c =image1.shape

#using image.shape to return height, width, and number of channels
boxes=pytesseract.image_to_boxes(image1)
for b in boxes.splitlines():
    b=b.split("")
    image1=cv2.rectangle(image1, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow("Image22", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
dict = pytesseract.image_to_data(image1, output_type= Output.DICT)
print(dict.keys())