"""
openai_utils.py
텍스트 요약을 위한 Azure OpenAI 유틸리티
"""
import requests
from utils.config import (
    AZURE_OPENAI_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT_NAME
)

def summarize_text_with_azure_openai(text):
    """
    Azure OpenAI를 사용해 텍스트를 요약합니다.
    Args:
        text (str): 요약할 텍스트
    Returns:
        str: 요약된 텍스트
    Raises:
        Exception: 요청 실패 시 예외 발생
    """
    url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT_NAME}/chat/completions?api-version=2024-03-01-preview"

    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_OPENAI_KEY
    }

    system_prompt = (
        "당신은 전문 문서 요약가입니다. 사용자가 제공한 긴 문서를 핵심만 간결하게 요약해 주세요. "
        "중요한 정보는 최대한 빠뜨리지 말고 명확하게 요약하세요."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"다음 문서를 요약해 주세요:\n\n{text}"}
    ]

    payload = {
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 1000
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"OpenAI 요청 실패: {response.status_code} - {response.text}")

    result = response.json()
    return result["choices"][0]["message"]["content"]
