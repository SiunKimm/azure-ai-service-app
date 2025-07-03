"""
pdf_utils.py
PDF 문서에서 텍스트를 추출하는 Azure Document Intelligence 유틸리티
"""
import requests
import time

def analyze_pdf_with_azure(file_path, endpoint, key):
    """
    Azure Document Intelligence를 사용해 PDF에서 텍스트를 추출합니다.
    Args:
        file_path (str): 분석할 PDF 파일 경로
        endpoint (str): Azure Form Recognizer 엔드포인트
        key (str): Azure Form Recognizer 키
    Returns:
        str: 추출된 전체 텍스트
    Raises:
        Exception: 요청 실패 또는 시간 초과 시 예외 발생
    """
    model = "prebuilt-document"
    api_version = "2023-07-31"
    url = f"{endpoint}/formrecognizer/documentModels/{model}:analyze?api-version={api_version}"

    headers = {
        "Content-Type": "application/pdf",
        "Ocp-Apim-Subscription-Key": key
    }

    with open(file_path, "rb") as f:
        data = f.read()

    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 202:
        raise Exception(f"Analyze request failed: {response.status_code} - {response.text}")

    # 결과 추적
    operation_url = response.headers["Operation-Location"]

    # 비동기 처리: 완료까지 대기
    for _ in range(10):
        result = requests.get(operation_url, headers={"Ocp-Apim-Subscription-Key": key})
        if result.status_code != 200:
            raise Exception(f"Status error: {result.status_code}")
        result_json = result.json()
        if result_json.get("status") == "succeeded":
            break
        time.sleep(2)
    else:
        raise TimeoutError("분석하는데 시간이 너무 오래 걸림")

    # 전체 텍스트 추출
    return result_json["analyzeResult"]["content"]
