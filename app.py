
"""
app.py
메인 실행 파일. Gradio UI를 통해 PDF 업로드, 요약, TTS까지 전체 파이프라인을 실행합니다.
"""
import gradio as gr
from utils.config import AZURE_FORM_KEY, AZURE_FORM_ENDPOINT
from utils.pdf_utils import analyze_pdf_with_azure
from utils.openai_utils import summarize_text_with_azure_openai
from utils.tts_utils import text_to_speech

def process_pdf(file):
    """
    업로드된 PDF 파일을 분석, 요약, 음성 변환하여 반환합니다.
    Args:
        file: 업로드된 PDF 파일 객체
    Returns:
        tuple: (요약 텍스트, mp3 파일 경로)
    """
    if file is None:
        return "No file uploaded.", None

    extracted_text = analyze_pdf_with_azure(file.name, AZURE_FORM_ENDPOINT, AZURE_FORM_KEY)
    summary = summarize_text_with_azure_openai(extracted_text)
    audio_path = text_to_speech(summary)

    return summary, audio_path

iface = gr.Interface(
    fn=process_pdf,
    inputs=gr.File(label="PDF 문서를 업로드하세요", file_types=[".pdf"]),
    outputs=[
        gr.Textbox(label="요약 결과"),
        gr.Audio(label="AI 요약 음성", type="filepath")
    ],
    title="Azure AI 문서 요약 + TTS",
    description="Azure Document Intelligence + OpenAI + Speech TTS로 PDF 문서를 요약하고, 음성으로 변환합니다."
)

if __name__ == "__main__":
    # share=True 옵션을 사용하면 외부에서도 접속 가능한 임시 링크가 생성됩니다.
    iface.launch(share=True)
