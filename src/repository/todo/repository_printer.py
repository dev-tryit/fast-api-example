from typing import List

from repository.todo.repository import TodoRepository
from repository.todo.scheme.todo_model import TodoModel


class TodoRepositoryPrinter(TodoRepository):
    def create(self, todo_model: TodoModel) -> TodoModel:
        print('create')

    def delete(self, todo_id: int) -> TodoModel | None:
        print('delete')

    def update(self, todo_model: TodoModel) -> TodoModel | None:
        print('update')

    def get(self, todo_id: int) -> TodoModel | None:
        print('get')

    def get_all(self) -> List[TodoModel]:
        print('get_all')
