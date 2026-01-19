import cv2
import numpy as np
import os

input_dir = r"merged_result"
output_dir = "result_otsu"
os.makedirs(output_dir, exist_ok=True)

for n in range(4, 5):
    img = cv2.imread(
        f"{input_dir}/sample_{n}.png",
        cv2.IMREAD_GRAYSCALE
    )

    if img is None:
        raise ValueError("이미지 로드 실패")

    # 1. Gaussian Blur
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    # 2. Otsu Threshold
    otsu_th, binary = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    print(f"[sample_{n}] Otsu threshold =", otsu_th)

    # 3. 저장
    cv2.imwrite(
        f"{output_dir}/sample_{n}.png",
        binary
    )
