from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"ping" : "pong"}

from fastapi import Depends
from database.connection import get_db
from sqlalchemy.orm import Session
from database.repository import get_todos
from typing import List
from database.orm import Todo
from scheme.response import TodoSchema, ListTodoResponse

@app.get("/todos")
def get_todos_handler(
    order: str| None = None,
    session: Session = Depends(get_db),
    
):
    todos:List[Todo] = get_todos(session=session)
    if order and order == "DESC":
        return ListTodoResponse(
        #리스트 컴프리헨션 ([expression for item in iterable])
        todos=[TodoSchema.from_orm(todo) for todo in todos[::-1] ]
    )
    return ListTodoResponse(
        #리스트 컴프리헨션 ([expression for item in iterable])
        todos=[TodoSchema.from_orm(todo) for todo in todos ]
    )
    

## GET API - 단일 조회 (중괄호 사이 변수 = path로 이용 가능)
## ex. localhost:8800/todos/2
from fastapi import HTTPException
@app.get("/todos/{todo_id}", status_code=200)
def get_todo_handler(todo_id: int):
    todo = todo_data.get(todo_id, {})
    if todo :
        return todo        
    raise HTTPException(status_code=404, detail="ToDo Not Found")

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


@app.post("/todos", status_code=201)
def create_todo_handler(request: CreateToDoRequest):
    todo_data[request.id] = request.dict()
    return todo_data[request.id]


## PATCH Method - 수정
#### is_done 값만을 업데이트 할 예정이라 위 post 메서드 처럼 request body를 전체를 전달하지 않고
#### is_done만 처리할 것이라 fastapi의 Body 모듈을 가져올 거임
from fastapi import Body
@app.patch("/todos/{todo_id}", status_code=200)
def update_todo_handler(
    todo_id: int,
    is_done: bool = Body(..., embed=True),
    ):
    todo = todo_data.get(todo_id)
    if todo:
        todo["is_done"] = is_done
        return todo
    raise HTTPException(status_code=404, detail="Todo Not Found")


## Delete Method - 삭제
@app.delete("/todos/{todo_id}", status_code="204")
def delete_todo_handler(todo_id: int):
    todo = todo_data.pop(todo_id, None)
    if todo :
        return
    
    raise HTTPException(404, "Not Found")