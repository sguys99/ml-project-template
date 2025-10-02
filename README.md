# ml-project-template

1. 파이썬 버전 설정
   uv python pin 3.12.9

2. 가상환경
   uv venv .venv

3. 진입
   source .venv/bin/activate

4. 의존성 설치 (uv sync)
   uv sync

5. 개발용 의존성 포함 설치
   uv sync --all-extras --dev
