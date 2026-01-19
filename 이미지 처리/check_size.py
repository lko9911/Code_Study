import cv2
import numpy as np

img_path = "image.png"

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError(f"이미지를 불러올 수 없습니다: {img_path}")

print("shape :", img.shape)   # (H, W)
print("size  :", img.size)    # H * W
print("dtype :", img.dtype)   # uint8
print("ndim  :", img.ndim)    # 2