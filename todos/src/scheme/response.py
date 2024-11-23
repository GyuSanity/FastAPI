from typing import List
from pydantic import BaseModel


# Response 를 위해 왜 다시 모델을 정의를 해야하는가?
# Response 객체를 분리해 놓으면 컬럼간의 연산이나 아이디나 이즈던값만 리턴하고 싶다하는 여러 유즈케이스에서
# 유연하게 변경이 가능함으로 분리해서 처리를 한다

# sqlalchemy의 orm 객체를 TodoSchema에게 던져지면,
# pydantic이 해당 orm 객체를 잘 해석을 해서 id/contents/is_done에 맞춰 파싱을 해줌
# ex. 
# >>> from database.orm import Todo
# >>> from scheme.response import TodoSchema
# >>>
# >>>
# >>> todo = Todo(id=100, contents="Test", is_done=True)
# >>> todo
# ToDo(id=100, contents=Test, is_done=True)
# >>> TodoSchema.from_orm(todo)
# TodoSchema(id=100, contents='Test', is_done=True)

class TodoSchema(BaseModel):
    id: int
    contents: str
    is_done: bool
    
    class Config :
        orm_mode = True
    

class ListTodoResponse(BaseModel):
    todos: List[TodoSchema]
    
