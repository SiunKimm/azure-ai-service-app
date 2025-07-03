"""
tts_utils.py
텍스트를 음성으로 변환하는 Azure Speech TTS 유틸리티
"""
import requests
from utils.config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION
import uuid
import xml.sax.saxutils as saxutils

def text_to_speech(text, voice="ko-KR-SunHiNeural", output_path=None):
    """
    Azure Speech TTS를 사용해 텍스트를 음성(mp3)으로 변환합니다.
    Args:
        text (str): 변환할 텍스트
        voice (str): 사용할 음성 이름
        output_path (str): 저장할 파일 경로 (None이면 자동 생성)
    Returns:
        str: 생성된 mp3 파일 경로
    Raises:
        ValueError: 입력 텍스트가 비어있을 때
        Exception: 요청 실패 시 예외 발생
    """
    if not text.strip():
        raise ValueError("텍스트가 비어있습니다.")

    endpoint = f"https://{AZURE_SPEECH_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"

    headers = {
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
        "Ocp-Apim-Subscription-Key": AZURE_SPEECH_KEY
    }

    safe_text = saxutils.escape(text)

    ssml = f"""
    <speak version='1.0' xml:lang='ko-KR'>
        <voice xml:lang='ko-KR' xml:gender='Female' name='{voice}'>
            {safe_text}
        </voice>
    </speak>
    """

    response = requests.post(endpoint, headers=headers, data=ssml.encode("utf-8"))
    if response.status_code != 200:
        raise Exception(f"TTS 요청 실패: {response.status_code} - {response.text}")

    filename = output_path or f"tts_{uuid.uuid4().hex[:8]}.mp3"
    with open(filename, "wb") as f:
        f.write(response.content)

    return filename
