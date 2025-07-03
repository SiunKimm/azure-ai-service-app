# Azure AI Service App
이 프로젝트는 Azure 기반의 AI 서비스를 활용한 데모 애플리케이션입니다.  
Gradio 인터페이스를 통해 PDF 분석, 텍스트 요약, 음성 변환을 간편하게 수행할 수 있습니다.
---
## 🔧 리팩터링 및 구조 개선 내역
- `utils/` 폴더로 기능별 유틸리티 모듈 분리
- 모든 주요 함수에 **docstring** 및 **한글 주석** 추가
- 환경 변수 로딩 로직을 `config.py`로 모듈화
- Gradio UI 인터페이스 및 전체 파이프라인에 주석 보강
---
## 💡 사용 기술
- **Python 3.11**
- **Gradio** (UI 프레임워크)
- **Azure AI Document Intelligence**
- **Azure OpenAI (Chat Completion)**
- **Azure Speech (Text-to-Speech)**
- `requests`, `python-dotenv` 등 보조 라이브러리
