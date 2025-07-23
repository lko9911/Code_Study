# 1. 특정 파일의 데이터 읽기
from glob import glob
import os

splits = 'A,B' # A,B만 다르고 나머지가 동일한 경로일 경우
for split in splits:
  dir = f"/content/{split}/..."
  paths = glob(f"{dir}/*.파일 형식")
  print(f"📂 디렉토리 경로: {dir}")
  print(f"🔍 검색한 파일의 수: len{paths}")

  if len(paths) > 0:
    print(f"📑 첫번째 파일 이름:", os.path.basename(paths[0]))
  else:
    print("파일 없음 !")

# 2. yolo 데이터셋 구성 자동화
import os
from glob import glob
from tqdm import tqdm
import shutil

src_img_root = '학습셋 이미지 주소'
src_label_root = '라벨이나 마스크 주소(txt라고 가정)'
dst_img_root = 'content/dataset/train/images'
dst_label_root = 'content/dataset/train/labels'

src_img_root_val = '검증셋 이미지 주소'
src_label_root_val = '라벨이나 마스크 주소(txt라고 가정)'
dst_img_root_val = 'content/dataset/val/images'
dst_label_root_val = 'content/dataset/val/labels'

os.makedirs(dst_img_root, exist_ok=True)
os.makedirs(dst_label_root, exist_ok=True)
os.makedirs(dst_img_root_val, exist_ok=True)
os.makedirs(dst_label_val, exist_ok=True)

def copy_img_label(image_dir,label_dir,dst_image_dir,dst_label_dir):
  image_paths = sorted(glob(os.path.join(image_dir,'*.png')) + glob(os.path.join(image_dir,'*.jpg'))) # png, jpg 둘다 형식 안가리고 가져옴, 수정할수 있음 / 이미지의 경로 모음

  for img_path in tqdm(image_paths): # tqdm 문법 공부하기
    img_name = os.path.basename(imp_path)
    name_ext = os.path.splitext(img_name)[0] # 이름 그대로 가져옴-yolo는 이미지와 라벨의 이름이 같아야 함

    shutil.copy(img_path, os.path.join(dst_image_dir,f"{name_ext}.txt")) # 얕은 복사라 해도됨, copy2는 메타데이터까지 복사

    label_path = os.path.join(label_dir,f"{name_ext}.txt")
    if os.path.exists(label_path):
      shutil.copy(label_path,os.path.join(dis_label_dir,f"{name_ext}.txt")) # if 뺴고 해도됨, 그냥 디버깅용으로 넣은 것

copy_img_label(src_img_root,src_label_root,dst_img_root,dst_label_root)
copy_img_label(src_img_root_val,src_label_root_val,dst_img_root_val,dst_label_root_val)
