from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from repo.todo.repository import TodoRepository
from repo.todo.scheme.todo_model import TodoModel


class TodoRepositoryMySql(TodoRepository):
    def create(self, session: Session, todo_model: TodoModel) -> TodoModel:
        session.add(instance=todo_model)
        session.commit()  # save
        session.refresh(instance=todo_model)  # read (load id)
        return todo_model

    def delete(self, session: Session, todo_id: int) -> TodoModel | None:
        todo_model = self.get(session, todo_id)
        if todo_model is None:
            return None

        session.delete(todo_model)
        session.commit()  # save

        deleted_todo_model = self.get(session, todo_id)
        if deleted_todo_model:
            return None

        return todo_model

    def update(self, session: Session, todo_model: TodoModel) -> TodoModel | None:
        session.add(instance=todo_model)
        session.commit()  # save
        session.refresh(instance=todo_model)  # read (load id)
        return todo_model

    def get(self, session: Session, todo_id: int) -> TodoModel | None:
        return session.scalar(select(TodoModel).where(TodoModel.id == todo_id))

    def get_all(self, session: Session) -> List[TodoModel]:
        return list(session.scalars(select(TodoModel)))
