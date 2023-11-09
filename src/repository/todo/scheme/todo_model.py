from sqlalchemy import Column, Integer, Boolean, String

from _common.connection.mysql_connection import Base


class ToDoModel(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"ToDoModel(id={self.id}, contents='{self.contents}', is_done={self.is_done})"

    def __str__(self):
        return f"ID: {self.id}\nContents: {self.contents}\nIs Done: {self.is_done}"
