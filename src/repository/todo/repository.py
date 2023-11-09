from abc import ABC, abstractmethod

from repository.todo.scheme.todo_model import TodoModel


class TodoRepository(ABC):
    @abstractmethod
    def create(self, todo_model: TodoModel):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_all(self):
        pass
