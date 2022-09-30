import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('D:\python\images\labka.jpg', 0)

#otsu = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU )
retval, otsu_threshold = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU,)
print("Obtained threshold: ", otsu_threshold)
plt.imshow(otsu_threshold)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()