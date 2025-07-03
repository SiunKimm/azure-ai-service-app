# utils 폴더
#
# - `config.py`: 환경 변수 로딩 및 Azure 키 관리
# - `pdf_utils.py`: PDF 텍스트 추출 함수
# - `openai_utils.py`: 텍스트 요약 함수
# - `tts_utils.py`: 텍스트 음성 변환 함수
#
# 리팩터링 및 구조 개선 내역
#
# - utils/ 폴더로 유틸리티 코드 분리 및 주석/문서화
# - .gitignore, requirements.txt, README.md, utils/README.md 추가
# - 모든 주요 함수에 docstring 및 한글 주석 추가
# - config, pdf_utils, openai_utils, tts_utils 등 모듈화
# - Gradio UI 및 전체 파이프라인 주석화