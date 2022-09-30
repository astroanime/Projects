import cv2
import numpy as np
import imutils

img = cv2.imread('D:\python\images\LicensePlate.jpg')

rotated = imutils.rotate(img, -15)
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()