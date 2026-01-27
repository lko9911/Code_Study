# 이진화 (Binary Thresholding)

import cv2
import numpy as np

img = cv2.imread("sample/sample.png", cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
