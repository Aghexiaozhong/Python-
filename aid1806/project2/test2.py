import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

for i in range(45):
    cap.read()

_, frame1 = cap.read()
cap.release()
time.sleep(0.1)

cv2.imshow('capture',frame1)
if cv2.waitKey(1) & 0xFF == ord('q'):
        pass
time.sleep(5)
time.sleep(10)

cv2.destroyAllWindows()
img_200x200 = cv2.resize(frame1, (960, 720))

cv2.imshow('capture',img_200x200)


if cv2.waitKey(1) & 0xFF == ord('q'):
        pass

time.sleep(5)

cap.release()
cv2.destroyAllWindows()
        

    
    
