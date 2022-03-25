import cv2
import datetime

cap=cv2.VideoCapture(0);

frame_width=print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=print(cap.get(cv2.CAP_PROP_FPS))

'''fourcc=cv2.VideoWriter_fourcc(*"avi")'''
'''out=cv2.VideoWriter("output.avi", fourcc, 30.0, (640,480))'''

cap.set(5,1920)
cap.set(6,1080)
print(cap.get(5))
print(cap.get(6))

while True:
    ret, frame=cap.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    font=cv2.FONT_HERSHEY_SIMPLEX
    text="Width: " + str(cap.get(5)) +  "Height: " + str(cap.get(6))
    datet=str(datetime.datetime.now())

    gray= cv2.putText(gray, datet, (10,50), font, 0.5, (0,255,255), 1, cv2.LINE_AA)
    '''out.write(frame)'''

    cv2.imshow("VIDEO",gray)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
'''out.release()'''
cv2.destroyAllWindows()

