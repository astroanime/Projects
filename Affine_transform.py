import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:\python\images\LicensePlate.jpg')
rows, cols, ch = img.shape

#left points
cv2.circle(img, (21, 72), 5,(0, 0, 255), -1)
cv2.circle(img, (21, 140), 5,(0, 0, 255), -1)
#right points
cv2.circle(img, (250, 74), 5,(0, 0, 255), -1)
cv2.circle(img, (255, 12), 5,(0, 0, 255), -1)

pts1 = np.float32([[21, 72], [21, 140],[250, 12],])

pts2 = np.float32([[0, 0 ], [0, 180], [280, 0],])


affine = cv2.getAffineTransform(pts1, pts2)
warp_affined = cv2.warpAffine(img, affine, (cols, rows))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')

plt.subplot(122)
plt.imshow(warp_affined)
plt.title('Output')
plt.show()


cv2.destroyAllWindows()