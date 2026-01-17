# 1. 라이브러리
import os
import openai
import pytchat # 유튜브용
from time import sleep
from gtts import gTTS
import pygame
from dotev import load_dotenv

load_dotenv() # env.용 API키 넣을것

# 1. OpenAI API 키 설정
openai.api_key = os.getenv("KEY1")

# 2. 유튜브 비디오 아이디
YOUTUBE = os.getenv("KEY2")

# 3.1. 디버깅용 파일 생성 1
TEXT_FILE = "get_response.txt"

# 3.2. 디버깅용 파일 생성 2
logging.basisConfig(
  filename = "get_response.txt"
  level=logging.WARNING,
  format=""
)
