import numpy as np
import cv2
from matplotlib import pyplot as plt

#Reading of the image
image = cv2.imread("shapes.jpg")

#Converting the image to gray scale image
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#setting the threshold of the gray image
_,thresh=cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
contours,_ =cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#List for storing names of the shapes
for contour in contours:
    #Using approxPolyDp to approximate the shape
    approx=cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(image, [approx], 0, (0,0,0), 3)

    #Finding center point of the shape

    #M=cv2.moments(contour)
    #if M["m00"]!=0.0:
        #x=int(M["m10"]/M["m00"])
        #y=int(M["m01"]/M["m00"])
    x= approx.ravel()[0]
    y=approx.ravel()[1]

    if len(approx) ==3:
        cv2.putText(image, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
    elif len(approx) ==4:
        x,y,w,h =cv2.boundingRect(approx)
        aspectRatio= float(w)/h
        print(aspectRatio)
        if aspectRatio >=0.95 and aspectRatio <=1.05:
            cv2.putText(image, "Square", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
        else:
            cv2.putText(image, "Quadrilateral", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

        
    elif len(approx) ==5:
        cv2.putText(image, "Pentagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
    elif len(approx) ==6:
        cv2.putText(image, "Hexagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
    elif len(approx) ==8:
        cv2.putText(image, "Octagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
    elif len(approx) ==10:
        cv2.putText(image, "Star", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
    else:
        cv2.putText(image, "Circle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)


cv2.imshow("Geometricshapes", image )

cv2.waitKey(0)
cv2.destroyAllWindows()