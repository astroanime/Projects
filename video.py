import cv2 as cv
import numpy as np
filename = 'video2.avi'
frames_per_seconds = 24.0
se = cv.VideoWriter_fourcc(*'XVID')

cap = cv.VideoCapture(0)
out = cv.VideoWriter(filename, se, frames_per_seconds, (640, 480) )
while(True):
    ret, frame = cap.read()
    hls = cv.cvtColor(frame, cv.COLOR_BayerRG2BGRA)
    out.write(frame)
    retval, threshed = cv.threshold(frame,100,150,cv.THRESH_BINARY)
    cv.imshow('yuv', hls)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()