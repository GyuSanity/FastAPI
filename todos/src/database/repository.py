## 레포지토리 패턴으로 작성
## 함수를 통해서 데이터 베이스를 조회하는걸 생성하고, 그 함수를 main.py에서 사용하도록 한다

from typing import List  ## 스탠다르 라이브러리에서 타입 힌트를 위해 지원

from sqlalchemy import select
from sqlalchemy.orm import Session
from database.orm import Todo

## Todo를 리스트에 담아서 Return을 함
def get_todos(session:Session) -> List[Todo]:
    return list(session.scalars(select(Todo)))