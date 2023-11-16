from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from repo.todo.scheme.todo_model import TodoModel


class TodoRepository(ABC):
    @abstractmethod
    def create(self, session: Session, todo_model: TodoModel) -> TodoModel:
        pass

    @abstractmethod
    def delete(self, session: Session, todo_id: int) -> TodoModel | None:
        pass

    @abstractmethod
    def update(self, session: Session, todo_model: TodoModel) -> TodoModel | None:
        pass

    @abstractmethod
    def get(self, session: Session, todo_id: int) -> TodoModel | None:
        pass

    @abstractmethod
    def get_all(self, session: Session):
        pass
