import cv2

cap=cv2.VideoCapture(0);

while True:
    ret,frame=cap.read()

    frame_width=print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height=print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps=print(cap.get(cv2.CAP_PROP_FPS))

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", gray)

    if cv2.waitKey(1) & 0XFF==ord("q"):
        break

cap.release()
cv2.destroyAllWiindows()



