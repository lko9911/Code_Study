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


