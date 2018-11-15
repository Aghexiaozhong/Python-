import cv2
import numpy as np
import time

cap = cv2.VideoCapture("./time_lapse.avi")

for i in range(500):
    ret,frame = cap.read()
    time.sleep(0.1)
    
    if frame==[]:
        break
    cv2.imshow("capture",frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
