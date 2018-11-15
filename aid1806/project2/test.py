import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

for i in range(20):
    cap.read()


_, frame1 = cap.read()

while True:

    time.sleep(0.1)

    _, frame2 = cap.read()
    cv2.imshow('capture',frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

    
    frame3=np.maximum(frame1,frame2)
    frame4=np.minimum(frame1,frame2)
    frame=np.subtract(frame3,frame4)

    a=frame.var()
    print('视频变化的方差：',a)
    frame1 = frame2
            


