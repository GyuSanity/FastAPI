from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"ping" : "pong"}


## GET Method - 전체 조회
## Dictionary 자료형 기본 Methods
# 2-1. dict.keys(): 사전의 키 목록
# 2-2. dict.values(): 사전의 값 목록
# 2-3. dict.items(): 사전의 (키, 값) 튜플 목록 
# 2-4. dict.clear(): 사전의 모든 {키, 값} 셋 제거
# 2-5. dict.copy(): 사전의 {키 : 값} 셋 복사
# 2-6. dict.fromkeys(seq, value): seq, value 셋으로 신규 사전 생성
# 2-7. dict.get(key, default=None): 키에 할당된 값 반환
# 2-8. dict.setdefault(key, default=None) : 키에 할당된 값 반환
# 2.9. dict.update(dict2): 기존 사전에 새로운 사전 dict2 추가
todo_data = {
    1: {
        "id":1,
        "contents":"실전! FastAPI 섹션 0 수강",
        "is_done": True,
    },
    2: {
        "id":2,
        "contents":"실전! FastAPI 섹션 0 수강",
        "is_done": True,
    },
    3: {
        "id":3,
        "contents":"실전! FastAPI 섹션 0 수강",
        "is_done": True,
    },
    4: {
        "id":4,
        "contents":"실전! FastAPI 섹션 0 수강",
        "is_done": True,
    },
}

@app.get("/todos")
def get_todos_handler() :
    return list(todo_data.values()) ## List 형태로 묶어줘야 에러가 없음

## GET Method - 전체 조회, 쿼리 파라미터 추가
## ex. localhost:8800/todos?order=DESC
@app.get("/todos")
def get_todos_handler(order: str| None = None):
    ret = list(todo_data.values())
    if order and order == "DESC" :
        return ret[::-1]
    return ret


## GET API - 단일 조회 (중괄호 사이 변수 = path로 이용 가능)
## ex. localhost:8800/todos/2
@app.get("/todos/{todo_id}")
def get_todo_handler(todo_id: int):
    return todo_data.get(todo_id, {})

## POST Method : post 생성
## 사용자로 부터 데이터(request body)를 받아야하는데,
## pydantic의 basemodel을 사용해서 request body를 처리할 예정
## ex.
#### BaseModel을 상속 받은 CreteToDoRequest 클래스를 생성 후,
#### post path의 함수 인자로 전달 시 fastAPI가 알아서 requestBody를 
#### CreateToDoRequest에 맞춰서 채워줌
#### 단, todo_data[request.id]의 Value는 dict로 선언되어 있어 request 클래스를 전달하면
####     type이 다르다고 에러가 남으로 dict()로 변환 필요(BaseModel에서 제공하는 메서드임)


from pydantic import BaseModel
class CreateToDoRequest(BaseModel):
    id : int
    contents: str
    is_done:bool


@app.post("/todos")
def create_todo_handler(request: CreateToDoRequest):
    todo_data[request.id] = request.dict()
    return todo_data[request.id]


##PATCH Method - 수정
