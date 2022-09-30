import cv2 as cv
import glob
import matplotlib.pyplot as plt

path = glob.glob('D:/python/images/original/*.jpg')
i=0
original = cv.imread('D:\python\images\labka.jpg')
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
for image in path:
    print(image)
    img = cv.imread(image)
    gray_images = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gray_images', gray_images)
    hist1 = cv.calcHist([gray], [0], None, [256], [0,255])
    hist2 = cv.calcHist([gray_images], [0], None, [256], [0,255])
    cv.normalize(hist1, hist1, 0, 255, cv.NORM_MINMAX)
    cv.normalize(hist2, hist2, 0, 255, cv.NORM_MINMAX)
    metric_val = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    i = i + 1
    print("For number", str(i) ,metric_val)
    plt.plot(hist1)
    plt.plot(hist2)
    cv.waitKey(600)
    cv.destroyAllWindows()

