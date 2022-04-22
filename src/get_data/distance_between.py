import time

import cv2

img = 'page.png'
img = cv2.imread(img)
cv2.imshow('original', img)
roi = cv2.selectROI(windowName="original", img=img, showCrosshair=True, fromCenter=False)
# roi = (727, 268, 310, 154)
x, y, w, h = roi
print(roi)
if roi != (0, 0, 0, 0):
    crop = img[y:y + h, x:x + w]
    cv2.imshow('crop', crop)
    cv2.imwrite('2.jpg', crop)
    print('Saved!')

# 退出
cv2.waitKey(0)
cv2.destroyAllWindows()
# (727, 268, 310, 154)
# (728, 265, 62, 157)
