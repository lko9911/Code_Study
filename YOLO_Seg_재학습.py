# YOLO_재학습 코드는 울트라틱스의 사전 학습 yolo 모델을 가져와 COLAB에서 학습 시킨다.
# COLAB 기준 YOLO의 경우 A100 GPU나 T4 GPU를 사용헤야 하며 A100이 조금더 빠르나 비용이 많이듦

## 울트리틱스 라이브러리 설치 (COLAB의 경우 무조건 설치해야 함)
!pip install ultralytics

## 1. 구글 마운트 (드라이브로 데이터셋 가져오기) or roboflow의 데이터셋을 가져오는 코드 - 공유 문서로 가져와도 됨
from google.colab import drive
drive.mount('/content/drive')

## 2. 재학습 코드 (2025년 7월 기준 최신화)
### 2.1 라이브러리 임포트
from ultralytics import YOLO 
from glob import glob
import os
import cv2
import numpy as np
from glob import glob

### 2.2 데이터셋 yaml 정의 (굉장히 중요한 부분으로 'images'라는 폴더이름을 꼭 맞추어야 함 - 울트라틱스 yolo 함수내에 하드코딩되어 있음)
#### yaml의 정의와 데이터셋 구성에 대해 조금더 구체화할 것 (라벨 정의 포함)
data_yaml = '''\
path: /content/drive/MyDrive/Dataset
train: train/images
val: val/images

names:
 0: label_names
'''

yaml_path = "dataset_name.yaml" # 경로 지정보다는 이름의 정의라고 봄
with open(yaml_path, 'w') as f: # yaml_path 의 내용 정의
  f.write(data_yaml)
  
### 2.3 데이터셋 구성 부분 (만약 마스크 데이터가 png일 경우 라벨을 txt 형태로 바꾸어야함. yolo-seg 8버전 이후) / txt로 이미 있거나 seg가 아닐경우 안써도 됨
def convert_mask_to_text(mask_path, txt_path, target_pixel_value=255, class_id=0):
 mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE) # 흑백으로 거져오기
 h, w = mask.shape

 binary = (mask == target_pixel_value).astype(np.uint8) * 255 # Boolearn 형태 (True = 255, False = 0)
 contours,_= cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 객체 경계 좌표 추출 (contours 값을 기록)

 
 with open(txt_path) as f:
  for cnt in contours:
   if len(cnt) < 3:
    continue # 폴리곤은 최소 3개의 점으로 경계를 나타냄
   normalized = [f"{pt[0][0] / w:.6f} {pt[0][1] / h:.6f}" for pt in cnt] # 사진의 비율에 맞게 기입, 중요
   line = f"{class_id}" + " ".join(normalized) + "\n" # 줄당 입력되어지는 단어
   f.write(line)

## 라벨 생성
splits = ['train', 'val']
for split in splits:
 mask_dir = f"/content/{split}/mask_path"
 label_dir = f"/content/{split}/labels"
 os.makedirs(labels_dir, exist_ok=True) # 파일 만들기

 mask_paths = glob(f"{mask_dir}"/*.png) # 파일 형식에 따라 다름, png 주의하기

 for i, mask_path in enumerate(mask_paths): # 파일 지정 이름 부분
  file_name = os.path.splitext(os.path.basename(mask_path))[0] # 파일이름은 GT와 동일해야함
  txt_path = os.path.join(label_dir,f"{file_name}".txt)

  if os.path.exists(txt_path):
   # print(f"[{i+1}/len(mask_paths)] {file_name}.txt 존재 확인됨 (계산 넘김)")
   continue

  convert_mask_to_txt(mask_path, txt_path) # mask_path의 for문 단위로 진행

### 3. 모델 가져오고 학습 (울트라틱스의 사이트 참고)

model = YOLO("yolo11n-seg.pt") # 가져오고 싶은 모델

model.train(data = data_yaml, epochs = 10, imgsz=512, batch_size=4) 
