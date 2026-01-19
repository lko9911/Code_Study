import os
import cv2

# ===== 설정 =====
SRC_ROOT = "test_sample"   # 원본 폴더
DST_ROOT = "test_sample_upscale"   # 결과 폴더
TARGET_SIZE = (1280, 1280)

IMG_EXTENSIONS = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff")


def upscale_and_copy_structure(src_root, dst_root):
    for root, dirs, files in os.walk(src_root):
        # A 기준 상대 경로
        rel_path = os.path.relpath(root, src_root)
        dst_dir = os.path.join(dst_root, rel_path)

        # 폴더 구조 생성
        os.makedirs(dst_dir, exist_ok=True)

        for file in files:
            if not file.lower().endswith(IMG_EXTENSIONS):
                continue

            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst_dir, file)

            img = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
            if img is None:
                print(f"❌ 읽기 실패: {src_path}")
                continue

            # 업스케일
            img_up = cv2.resize(
                img,
                TARGET_SIZE,
                interpolation=cv2.INTER_CUBIC
            )

            cv2.imwrite(dst_path, img_up)
            print(f"✅ {dst_path}")


if __name__ == "__main__":
    upscale_and_copy_structure(SRC_ROOT, DST_ROOT)
    print("모든 작업 완료.")