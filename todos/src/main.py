from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"ping" : "pong"}


## GET API 전체 조회
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

# @app.get("/todos")
# def get_todos_handler() :
#     return list(todo_data.values()) ## List 형태로 묶어줘야 에러가 없음

#쿼리 파라미터 추가 - 인자로 전달
@app.get("/todos")
def get_todos_handler(order:str="") :
    ret = list(todo_data.values())
    if order == "DESC" :
        return ret[::-1]
    return ret


## GET API 단일 조회