"""
config.py
환경 변수 로딩 및 Azure 관련 키/엔드포인트 관리
"""
import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# Document Intelligence (PDF 추출)
AZURE_FORM_KEY = os.getenv("AZURE_FORM_KEY")
AZURE_FORM_ENDPOINT = os.getenv("AZURE_FORM_ENDPOINT")

# OpenAI (요약)
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Speech TTS
AZURE_SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")
