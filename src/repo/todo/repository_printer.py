from typing import List

from sqlalchemy.orm import Session

from repo.todo.repository import TodoRepository
from repo.todo.scheme.todo_model import TodoModel


class TodoRepositoryPrinter(TodoRepository):
    def create(self, session: Session, todo_model: TodoModel) -> TodoModel:
        print('create')
        return TodoModel()

    def delete(self, session: Session, todo_id: int) -> TodoModel | None:
        print('delete')
        return None

    def update(self, session: Session, todo_model: TodoModel) -> TodoModel | None:
        print('update')
        return None

    def get(self, session: Session, todo_id: int) -> TodoModel | None:
        print('get')
        return None

    def get_all(self, session: Session) -> List[TodoModel]:
        print('get_all')
        return []
