# 1. YOLO 관련 문서

### 참고사이트 : https://docs.ultralytics.com/ko/
### 데이터셋 사이트 : https://docs.ultralytics.com/ko/datasets/#contribute-new-datasets

데이터셋 구성
<pre><code>dataset/
├── train/
│   ├── images/
│   └── labels/
└── val/
    ├── images/
    └── labels/</code></pre>
    
⚠️ 데이터셋 구성 보다는 "train, val, images, labels 문서 이름 형식을 지켜야함
- 데이터셋 구성 자체는 코드로 새로 바꾸거나 참조 경로만 바꾸면 해결됨 (대신 images와 labels는 같은 train/val 구성에 있어야 함)
