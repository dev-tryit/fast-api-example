from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from _common.decorator.singleton import singleton


@singleton
class MysqlUtil:

    def __init__(self):
        self.DATABASE_URL = "mysql+pymysql://root:q1w2e3r4!@127.0.0.1:3306/fast_api_example"
        self.Base = declarative_base()
        self.engine = create_engine(
            self.DATABASE_URL,
            echo=True,
            # pool_recycle=3600,
            # pool_size=5,
        )
        self.Base.metadata.create_all(bind=self.engine)
        self.SessionFactory = None

    async def init_db(self):
        self.SessionFactory = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

    # 이터레이터 패턴을 통해서, 정리를 깔끔하게 할 수 있음.
    # Depends와 함께 쓰면, Request 당 Session 1개를 생성 가능
    # Depends가 get_session 함수를 반환할 때, session.close()가 실행됨
    @contextmanager
    def make_session(self):
        session: Session = self.SessionFactory()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
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
