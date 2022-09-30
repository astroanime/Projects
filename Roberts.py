import sys
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import io
import cv2

roberts_cross_v = np.array([[0, 0, 0],
                            [0, 1, 0],
                            [0, 0, -1]])

roberts_cross_h = np.array([[0, 0, 0],
                            [0, 0, 1],
                            [0, -1, 0]])

img = io.imread('D:\python\images\labka.jpg', 0)
img = cv2.GaussianBlur(img, (3, 3), 2)
img = img.astype('float64')
gray_img = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
gray_img /= 255

vertical = ndimage.convolve( gray_img, roberts_cross_v )
horizontal = ndimage.convolve( gray_img, roberts_cross_h )

edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))

plt.imshow(edged_img, cmap=plt.get_cmap('gray'))
plt.show()