from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 인증 정보를 상수로 생성
## mysql과 pymysql을 사용하며,
## 루트계정으로 투두스 비밀번호를 이용하여,
## 127.0.0.1:3306 포트에 접근하여
## todos 데이터 베이스를 이용한다
DATABASE_URL = "mysql+pymysql://root:todos@127.0.0.1:3306/todos"

engine = create_engine(DATABASE_URL, echo=True) # query과 사용되는 시점에 해당 sql을 print해줌(디버깅 용도로 사용)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine) #세션을 만들어 DB에 접근할수 있음

## 동작 확인
# (todos) gyyeon@DESKTOP-A9M7R8S:~/Git/FastAPI/todos/src$ python
# >>> from database.connection import SessionFactory
# >>> session = SessionFactory()
# >>> from sqlarchemy import select 
# >>> from sqlalchemy import select 
# >>> #태스트 동작 확인 
# >>> session.scalar(select(1))                                                             
# 2024-11-10 12:59:07,826 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2024-11-10 12:59:07,826 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2024-11-10 12:59:07,828 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2024-11-10 12:59:07,828 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2024-11-10 12:59:07,829 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2024-11-10 12:59:07,829 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2024-11-10 12:59:07,831 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-11-10 12:59:07,832 INFO sqlalchemy.engine.Engine SELECT 1
# 2024-11-10 12:59:07,832 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}