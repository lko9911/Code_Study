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
  
