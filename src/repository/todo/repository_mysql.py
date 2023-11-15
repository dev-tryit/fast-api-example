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

    def create(self, todo_model: TodoModel) -> TodoModel:
        self.session.add(instance=todo_model)
        self.session.commit()  # save
        self.session.refresh(instance=todo_model)  # read (load id)
        return todo_model

    def delete(self, todo_id: int) -> TodoModel | None:
        todo_model = self.get(todo_id)
        if todo_model is None:
            return None

        self.session.delete(todo_model)
        self.session.commit()  # save

        deleted_todo_model = self.get(todo_id)
        if deleted_todo_model:
            return None

        return todo_model

    def update(self, todo_model: TodoModel) -> TodoModel | None:
        self.session.add(instance=todo_model)
        self.session.commit()  # save
        self.session.refresh(instance=todo_model)  # read (load id)
        return todo_model

    def get(self, todo_id: int) -> TodoModel | None:
        return self.session.scalar(select(TodoModel).where(TodoModel.id == todo_id))

    def get_all(self) -> List[TodoModel]:
        return list(self.session.scalars(select(TodoModel)))
