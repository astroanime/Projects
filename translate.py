import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
from googletrans import Translator
import glob

path = glob.glob('D:/python/images/past/*.png')
for IMAGE_PATH in path:
    img = cv2.imread(IMAGE_PATH)
    reader = easyocr.Reader(['id'], gpu=True)
    result = reader.readtext(IMAGE_PATH, detail=0)
    trans = Translator()
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    result = reader.readtext(IMAGE_PATH)
    for detection in result:
        top_left = tuple([int(val) for val in detection[0][0]])
        bottom_right = tuple([int(val) for val in detection[0][2]])
        bottom_left = tuple([int(val) for val in detection[0][3]])
        test_tup2 = (35,0)
        res = tuple(map(lambda i, j: i - j, bottom_left, test_tup2))
        text = detection[1]
        text = trans.translate(text, dest="en")
        img = cv2.rectangle(img, top_left, bottom_right, (255, 255, 255), -1)
        img = cv2.putText(img, text.text, res, font,
                        1.5, (0, 0, 0), 3, cv2.LINE_AA)

    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.show()