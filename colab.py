# 마운트 코드

from google.colab import drive
drive.mount('/content/drive')

# 정보 저장 코드 (드라이브)

import shutil
import os

# 원본 경로
src = ""

# Drive에 저장될 경로 (이름 지정)
dst = "/content/drive/MyDrive/"

# 이미 존재하면 삭제 (선택)
if os.path.exists(dst):
    shutil.rmtree(dst)

# 복사
shutil.copytree(src, dst)

print("구글 드라이브 저장 완료:", dst)