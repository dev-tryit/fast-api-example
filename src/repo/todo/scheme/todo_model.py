from sqlalchemy import Column, Integer, Boolean, String

from _common.util.mysql_util import MysqlUtil
from domain.self_management.scheme.todo_vo import TodoVo


class TodoModel(MysqlUtil().Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"TodoModel(id={self.id}, contents='{self.contents}', is_done={self.is_done})"

    def __str__(self):
        return f"ID: {self.id}\nContents: {self.contents}\nIs Done: {self.is_done}"

    @classmethod
    def make(cls, *, contents, is_done) -> "TodoModel":
        return cls(
            contents=contents,
            is_done=is_done,
        )

    # noinspection PyTypeChecker
    def to_vo(self):
        return TodoVo(
            id=self.id,
            contents=self.contents,
            is_done=self.is_done,
        )

    def change_is_done(self, is_done: bool):
        self.is_done = is_done
        return self
