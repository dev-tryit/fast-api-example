from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import declarative_base

from _common.database.mysql_connection import engine

Base = declarative_base()
Base.metadata.create_all(bind=engine)


class ToDoModel(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"ToDoModel(id={self.id}, contents='{self.contents}', is_done={self.is_done})"

    def __str__(self):
        return f"ID: {self.id}\nContents: {self.contents}\nIs Done: {self.is_done}"
