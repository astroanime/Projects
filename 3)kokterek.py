import cv2 as cv
import numpy as np

image = cv.imread('D:\python\images\kokserek.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
retval, otsu_threshold = cv.threshold(
    gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU,)
gaus = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 5)
gaus_otsu = cv.adaptiveThreshold(
    otsu_threshold, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 5)
#cv.imshow('gray', gray)
#cv.imshow('image', image)
cv.imshow('Otsu', gaus_otsu)
cv.imshow('Guss', gaus)
cv.waitKey(0)
cv.destroyAllWindows()
