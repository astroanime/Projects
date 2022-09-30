#from sklearn.cluster import MiniBatchKMeans
import numpy as np
import cv2
import random
from PIL import Image
import PIL

#Task 3 code for Gaussian and "Salt & Pepper
def sp_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
#source
img = Image.open(r"D:\python\images\labka.jpg")
image = cv2.imread('D:\python\images\labka.jpg')

#converting to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#quantized image
image_quantized = img.quantize()
#2) Convert uploaded image to CMY, YUV and HLS color spaces
hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

#adding noisses
noise = sp_noise(image, 0.1)

#smoothing
smoothed = cv2.boxFilter(noise, 0, (5, 5))

cv2.imshow("image", image)
cv2.imshow('Gray image', gray)



image_quantized.show()

cv2.imshow('noise', noise)
cv2.imshow('filtered', smoothed)
cv2.imshow('cmy', hls)
cv2.imshow('yuv', yuv)




cv2.waitKey(0)
cv2.destroyAllWindows()
