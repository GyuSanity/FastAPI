## How to Create Env

python -m venv todo
cd example
source bin/activate

pip install fastapi==0.97.0 #=> fastapi 최신 버전을 인스톨 할 경우, fastapi가 pydantic v2를 사용
\+ 만약 pydantic v2를 사용하고 싶은 분들은 아래 문서를 참고해서 migration을 진행

- V2 migration: https://docs.pydantic.dev/latest/migration/

pip install unicorn #=> fastAPI를 동작 시키기 위해 필요한 라이브러리

# Pyhon 경로를 default로 잡고 있어 가상환경의 경로로 인터프리터 설정 필요

> Ctrl + Shipt + P
> python:select Interpreter 설정
