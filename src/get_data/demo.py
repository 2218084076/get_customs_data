import cv2
import numpy as np


def mark_edge(image_path: str):
    p = cv2.imread(image_path)
    hsv = cv2.cvtColor(p, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([0, 0, 255])  # 提取颜色的低值
    high_hsv = np.array([180, 30, 255])
    mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
    ret, binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(p, contours, -1, (0, 0, 255), 3)
    c = list(contours)
    for n in c:
        print(len(n))
    c_max = max(c, key=len)
    print('max\t', len(c_max))
    x = c_max[len(c_max) - 1][0][0]
    print(f'x={x}', type(x))


mark_edge('1.jpg')


def contour():
    im = cv2.imread('1.jpg')
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
    cv2.imshow('im', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
