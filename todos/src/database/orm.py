from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

# 테이블을 클래스로 모델링(declarative_base를 사용)
## declarative_base를 상속 받고
## container = todos
## table = todo
Base = declarative_base()
class Todo(Base):
    __tablename__ = "todo"    
    
    ## 아래와 같은 데이터 베이스 테이블 설정을 클래스화
    ## SHOW databases;
    ## USE todos;
    ## CREATE TABLE todo(
    ## id INT NOT NULL AUTO_INCREMENT,
    ## contents VARCHAR(256) NOT NULL,
    ## is_done BOOLEAN NOT NULL,
    ## PRIMARY KEY (id)
    ## );
    ## INSERT INTO todo (contents, is_done) VALUES ("FastAPI Section 0", true);
    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)
    
    ## (디버깅 용도)
    ## 객체 출력을 더 보기 쉽게 하기 위해 __repr__매직 메서드를 오버롸이트 해서 사용
    def __repr__(self):
        return f"ToDo(id={self.id}, contents={self.contents}, is_done={self.is_done})"
    
## 작성된 코드 동작 확인
# >>> from database.connection import SessionFactory
# >>> session = SessionFactory()
# >>> from sqlalchemy import select 
# >>> todos = list(session.scalar(select(ToDo)))
# >>> for todo in todos:
# ...     print(todo)
# ToDo(id=1, contents=FastAPI Section 0, is_done=True)
# ToDo(id=2, contents=FastAPI Section 1, is_done=True)
# ToDo(id=3, contents=FastAPI Section 2, is_done=True)
    

    
    