import cv2
import numpy as np
import os

input_dir = "merged_result"
output_dir = "result_merged"

os.makedirs(output_dir, exist_ok=True)

for n in range(4, 5):
    img = cv2.imread(
        f"{input_dir}/sample_{n}.png",
        cv2.IMREAD_GRAYSCALE
    )

    img = np.where(img >= 200, 255, 0).astype(np.uint8)


    cv2.imwrite(
        f"{output_dir}/sample_{n}.png",
        img
    )
