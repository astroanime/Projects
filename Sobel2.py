import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image_original = cv2.imread('building.jpg', cv2.IMREAD_COLOR)
# Convert image to gray scale
image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
# 3x3 Y-direction  kernel
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
# 3 X 3 X-direction kernel
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

filtered_image_y = cv2.filter2D(image_gray, -1, sobel_y)
filtered_image_x = cv2.filter2D(image_gray, -1, sobel_x)

(fig, (ax1, ax2, ax3)) = plt.subplots(1, 3, figsize=(25, 25))
ax1.title.set_text('Original Image')
ax1.imshow(image_original)
ax2.title.set_text('sobel_x')
ax2.imshow(filtered_image_y)
ax3.title.set_text('sobel_y filter')
ax3.imshow(filtered_image_x)
plt.show()