import cv2 
import numpy as np


img = cv2.imread('D:\python\images\LicensePlate.jpg', 0)
#left points
cv2.circle(img, (21, 72), 5,(0, 0, 255), -1)
cv2.circle(img, (21, 140), 5,(0, 0, 255), -1)
#right points
cv2.circle(img, (250, 74), 5,(0, 0, 255), -1)
cv2.circle(img, (255, 12), 5,(0, 0, 255), -1)
width, height = 277, 148

pts1 = np.float32([[21, 72], [21, 140],[250, 12], [255, 74]])
pts2 = np.float32([[0, 0 ], [0, width], [300, 0], [width, 300]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, matrix, (400, 400))

cv2.imshow('img', img)
cv2.imshow('Frameperspective', result)
cv2.waitKey(0)

