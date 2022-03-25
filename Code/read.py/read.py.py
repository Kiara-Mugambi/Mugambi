import cv2

cap=cv2.VideoCapture(0);
frame_width=cv2.CAP_PROP_FRAME_WIDTH
frame_height=cv2.CAP_PROP_FRAME_HEIGHT
fourcc=cv2.VideoWriter_fourcc(*'mkv')
out=cv2.VideoWriter("output.avi", fourcc, frame_width,frame_height)

while True:
    ret, frame=cap.read()

    out.write(frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", frame)
    

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()