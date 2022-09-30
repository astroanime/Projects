import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('D:\python\images\labka.jpg',0)
img = cv.GaussianBlur(img, (3, 3), 0,5)
# The input of Canny is ----->>>output of Canny 
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()