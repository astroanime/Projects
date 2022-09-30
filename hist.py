import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('D:\python\images\labka.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
dst = cv.calcHist(gray, [0], None, [256], [0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram for gray scale image')
plt.show()
cv.imshow('image',img)
cv.imshow('gray', gray)
cv.waitKey(0)
cv.destroyAllWindows()
