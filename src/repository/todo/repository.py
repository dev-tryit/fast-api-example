from abc import ABC, abstractmethod

from repository.todo.scheme.todo_model import TodoModel


class TodoRepository(ABC):
    @abstractmethod
    def create(self, todo_model: TodoModel) -> TodoModel | None:
        pass

    @abstractmethod
    def delete(self, todo_id: int) -> TodoModel | None:
        pass

    @abstractmethod
    def update(self, todo_model: TodoModel) -> TodoModel | None:
        pass

    @abstractmethod
    def get(self, id: int) -> TodoModel | None:
        pass

    @abstractmethod
    def get_all(self):
        pass
