# 1. 라이르러리
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

