# 1. 라이러러리
import os
import cv2
import torch
import numpy as np
from torch.utils.data import DataLoader, Dataset
import torchvision.trasforms as transforms
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim
import tqdm import tqdm
import albumentations as A
from albumentations.pytorch import ToTensorV2
import matplotlib.pyplot as plt

# 2. 사용할 데이터셋 정의
Class Dataset(Dataset):
  def __init__(self, images_dir, labels_dir, transform=None):
    self.images_dir = images_dir
    self.labels_dir = labels_dir
    self.transform = transform

    # 이미지 및 라벨 파일 목록 생
    self.images_files = sorted(os.listdir(images_dir))
    # self.labels_dir = sorted(os.listdir(labels_dir))
    self.labels_files = sorted([
      f for f in os.listdir(labels_dir)
      if f.endswith('png') # 파일 형신 지정하기, 필요 없으면 위에 주석으로
    ])

  def __len__(self):
    return len(self.image_files) # 이미지 파일 수 세기

  def __getitem__(self, idx):
    # 이미지 로드
    image_path = os.path.join(self.image_dir, self.image_files[idx])
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # 중요, 잊으면 나중에 디버깅 힘듦

    # 라벨 로드
    label_path = os.path.join(self.labels_dir, self.label_files[idx])
    label = cv2.imread(label_path, cv2.IMREAD_COLOR) # 색상 이미지 로드

    '''
    마스크 변환. 필요시 할것  (대개 세그먼트는 마스크를 쓰기 때문에 사용해야하지만, 이미 처리되었으면 할필요 없음)
    if self.transform:
      augmented = self.transform(image=image, mask=label)
      image = augmented['image']
      label = augmented['mask']

    return image, label.clone().detach().long() # label을 텐서 복제한(새로 복제) 후, 계산 그래프에서 분리 (역전파 영향 x), 자료형은 long으로 - 교차엔트로피 계산 때문에 long으로 지정
    '''

# 3.데이터셋 경로 지정
train_imges_dir = "content/train/images"
train_labels_dir = "content/train/lables"
val_imges_dir = "content/val/images"
val_imges_dir = "content/val/labels"
