import numpy as np
import cv2

cap = cv2.VideoCapture('walking.avi')


method = 1

if method == 0:
    bgSubtractor = cv2.bgsegm.createBackgroundSubtractorMOG()
elif method == 1:
    bgSubtractor = cv2.createBackgroundSubtractorMOG2()
else:
    bgSubtractor = cv2.bgsegm.createBackgroundSubtractorGMG()


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 3))
while True:
       ret , frame = cap.read()
    
    if ret:
        foregroundMask = bgSubtractor.apply(frame)
        foregroundMask = cv2.morphologyEx(foregroundMask, cv2.MORPH_OPEN, kernel)
        cv2.imshow('background subtraction', foregroundMask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
