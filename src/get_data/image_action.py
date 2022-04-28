import cv2
import numpy as np


def image_action(image_path: str):
    img = cv2.imread(image_path)
    cv2.imshow('original', img)
    # roi = cv2.selectROI(windowName="original", img=img, showCrosshair=True, fromCenter=False)
    roi = (727, 268, 310, 154)
    x, y, w, h = (727, 268, 310, 154)
    print(roi)
    if roi != (0, 0, 0, 0):
        crop = img[y:y + h, x:x + w]
        cv2.imshow('crop', crop)
        cv2.imwrite('1.jpg', crop)
        print('Saved!')

image_action('page.png')

src = cv2.imread("1.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
"""
提取图中的红色部分
"""
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
low_hsv = np.array([0, 0, 221])
high_hsv = np.array([180, 30, 255])
mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
cv2.imshow("test", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
