
import cv2

img=cv2.imread("RobertDunn-pagecontent2016.jpg",0)
cv2.imshow("Image",img)

cv2.waitKey(1)
cv2.destroyAllWindows()