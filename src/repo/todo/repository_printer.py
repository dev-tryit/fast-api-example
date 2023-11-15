from typing import List

from repo.todo.repository import TodoRepository
from repo.todo.scheme.todo_model import TodoModel


class TodoRepositoryPrinter(TodoRepository):
    def create(self, todo_model: TodoModel) -> TodoModel:
        print('create')
        return TodoModel()

    def delete(self, todo_id: int) -> TodoModel | None:
        print('delete')
        return None

    def update(self, todo_model: TodoModel) -> TodoModel | None:
        print('update')
        return None

    def get(self, todo_id: int) -> TodoModel | None:
        print('get')
        return None

    def get_all(self) -> List[TodoModel]:
        print('get_all')
        return []
