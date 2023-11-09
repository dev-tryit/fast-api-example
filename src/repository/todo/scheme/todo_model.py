from sqlalchemy import Column, Integer, Boolean, String

from _common.connection.mysql_connection import Base


class TodoModel(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"TodoModel(id={self.id}, contents='{self.contents}', is_done={self.is_done})"

    def __str__(self):
        return f"ID: {self.id}\nContents: {self.contents}\nIs Done: {self.is_done}"

    @classmethod
    def create(cls, *, contents, is_done) -> "TodoModel":
        return cls(
            contents=contents,
            is_done=is_done,
        )
