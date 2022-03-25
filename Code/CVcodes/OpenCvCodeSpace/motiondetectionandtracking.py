#################### Motion detection and tracking of persons################
#################### Gaussian blurring to identify persons ##################

import cv2

import numpy as np
import matplotlib as plt

cap= cv2.VideoCapture("pedestrians.mp4")

frame_width=print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=print(cap.get(cv2.CAP_PROP_FPS))

ret, frame1 = cap.read()
ret, frame2 =cap.read()


while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    frame_gray= cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(frame_gray, (5,5), 0)
    _, thresh=cv2.threshold(frame_gray, 20, 255, cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh, None, iterations=3)
    contours, _= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("Number of Contours = " +str(len(contours)))
    
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)

        if cv2.contourArea(contour) <2000:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1, "Status: {}".format("Movement"), (10,20),cv2.FONT_HERSHEY_SIMPLEX,
        1, (0,0,255), 3)
    #cv2.drawContours(frame1, contours, -1, (0,255,0), 3)

    cv2.imshow("VideoCapture", frame1)
    frame1=frame2
    ret, frame2= cap.read()

    if cv2.waitKey(40)==27:
        break

cv2.destroyAllWindows()
cap.release()