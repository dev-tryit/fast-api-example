from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from _common.decorator.singleton import singleton


@singleton
class MysqlUtil:
    DATABASE_URL = "mysql+pymysql://root:q1w2e3r4!@127.0.0.1:3306/fast_api_example"

    engine = create_engine(
        DATABASE_URL,
        echo=True,
        # pool_recycle=3600,
        # pool_size=5,
    )
    Base = declarative_base()
    Base.metadata.create_all(bind=engine)
    SessionFactory = sessionmaker(bind=engine, autocommit=False, autoflush=False, )

    # 이터레이터 패턴을 통해서, 정리를 깔끔하게 할 수 있음.
    # Depends와 함께 쓰면, Request 당 Session 1개를 생성 가능
    def get_session(self):
        session = self.SessionFactory()
        try:
            yield session
        finally:
            session.close()

    # interpreter 로 연결 확인 방법
    # from _common.util.mysql_connection import SessionFactory
    # session = SessionFactory()
    # from sqlalchemy import select
    # session.scalar(select(1))
    #
    # from repo.todo.todo_model import TodoModel
    # session.scalars(select(TodoModel))
