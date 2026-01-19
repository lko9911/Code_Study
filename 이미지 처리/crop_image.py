import cv2
import os

img_path = r"image.png"
output_dir = "output_split"
os.makedirs(output_dir, exist_ok=True)

img = cv2.imread(img_path)

# ✅ 1. 이미지 로드 확인
if img is None:
    raise ValueError(f"이미지를 불러오지 못했습니다: {img_path}")

h, w = img.shape[:2]
print("Image size:", w, h)

# ✅ 2. 사이즈 확인
if h != 1280 or w != 1280:
    raise ValueError("입력 이미지가 1280x1280이 아닙니다")

half = 640

patches = [
    img[0:half, 0:half],
    img[0:half, half:w],
    img[half:h, 0:half],
    img[half:h, half:w],
]

name = os.path.splitext(os.path.basename(img_path))[0]

for i, patch in enumerate(patches, 1):

    # ✅ 3. patch empty 체크
    if patch.size == 0:
        raise ValueError(f"patch {i}가 비어 있습니다")

    patch = cv2.resize(patch, (1280, 1280), interpolation=cv2.INTER_NEAREST)

    cv2.imwrite(
        os.path.join(output_dir, f"{name}_q{i}.png"),
        patch
    )
