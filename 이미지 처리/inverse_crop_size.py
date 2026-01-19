import cv2
import numpy as np
import os

input_dir  = "output_split_4_gassian"
output_dir = "result"
os.makedirs(output_dir, exist_ok=True)

base_name = "sample"
blend_width = 80   

# --------------------------------------------------
# 1. patch 로드
# --------------------------------------------------
patches = []
for i in range(1, 5):
    path = os.path.join(input_dir, f"{base_name}_4_q{i}.png")
    img = cv2.imread(path)

    if img is None:
        raise ValueError(f"이미지 로드 실패: {path}")

    patches.append(img.astype(np.float32))

# --------------------------------------------------
# 2. 가로 방향 블렌딩
# --------------------------------------------------
def blend_horizontal(left, right, blend_width=80):
    h, w, c = left.shape
    alpha = np.linspace(0, 1, blend_width).reshape(1, -1, 1)

    blended = left.copy()
    blended[:, -blend_width:] = (
        left[:, -blend_width:] * (1 - alpha) +
        right[:, :blend_width] * alpha
    )

    return np.hstack([blended, right[:, blend_width:]])

def blend_vertical(top, bottom, blend_width=80):
    h, w, c = top.shape
    alpha = np.linspace(0, 1, blend_width).reshape(-1, 1, 1)

    blended = top.copy()
    blended[-blend_width:, :] = (
        top[-blend_width:, :] * (1 - alpha) +
        bottom[:blend_width, :] * alpha
    )

    return np.vstack([blended, bottom[blend_width:, :]])


top = blend_horizontal(patches[0], patches[1], blend_width)
bottom = blend_horizontal(patches[2], patches[3], blend_width)

# --------------------------------------------------
# 3. 세로 방향 블렌딩
# --------------------------------------------------
merged = blend_vertical(top, bottom, blend_width)

merged = np.clip(merged, 0, 255).astype(np.uint8)
print("Merged size:", merged.shape)  # 대략 (2560, 2560)

# --------------------------------------------------
# 4. 단 한 번만 다운스케일
# --------------------------------------------------
merged_1280 = cv2.resize(
    merged,
    (1280, 1280),
    interpolation=cv2.INTER_AREA
)

cv2.imwrite(
    os.path.join(output_dir, f"{base_name}_merged.png"),
    merged_1280
)
