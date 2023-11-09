from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from _common.connection.mysql_connection import get_session
from repository.todo.repository import TodoRepository
from repository.todo.scheme.todo_model import TodoModel


class TodoRepositoryMySql(TodoRepository):
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, todo_model: TodoModel):
        self.session.add(instance=todo_model)
        self.session.commit()  # save
        self.session.refresh(instance=todo_model)  # read (load id)
        return todo_model

    def delete(self):
        print('delete')

    def update(self):
        print('update')

    def get(self):
        print('get')

    def get_all(self) -> List[TodoModel]:
        return list(self.session.scalars(select(TodoModel)))
