## How to Create Env

python -m venv todo
cd example
source bin/activate

pip install fastapi==0.97.0 #=> fastapi 최신 버전을 인스톨 할 경우, fastapi가 pydantic v2를 사용
\+ 만약 pydantic v2를 사용하고 싶은 분들은 아래 문서를 참고해서 migration을 진행

- V2 migration: https://docs.pydantic.dev/latest/migration/

pip install uvicorn #=> fastAPI를 동작 시키기 위해 필요한 라이브러리

# Pyhon 경로를 default로 잡고 있어 가상환경의 경로로 인터프리터 설정 필요

> Ctrl + Shipt + P
> python:select Interpreter 설정

## Uvicorn 실행

#src 경로 이동 후,

```bash
python -m uvicorn main:app --port 8800 --reload
```

## 디펜던시 파일 만들기

pip freeze > requirements.txt

## 디펜던시 파일로 프로젝트 필요 프로그램 다운로드 받기

pip install -r requirements.txt

---

## MySQL 도커 이미지로 실행

```bash
# Docker 명령어
docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=todos -e MYSQL_DATABASE=todos -d -v todos:/db --name todos mysql:8.0
docker ps
docker logs todos
docker volume ls

# MySQL 접속
docker exec -it todos bash
mysql -u root -p

# SQL
SHOW databases;
USE todos;
CREATE TABLE todo(
id INT NOT NULL AUTO_INCREMENT,
contents VARCHAR(256) NOT NULL,
is_done BOOLEAN NOT NULL,
PRIMARY KEY (id)
);

INSERT INTO todo (contents, is_done) VALUES ("FastAPI Section 0", true);
SELECT \* FROM todo;
```
