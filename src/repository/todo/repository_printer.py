from repository.todo.repository import TodoRepository
from repository.todo.scheme.todo_model import TodoModel


class TodoRepositoryPrinter(TodoRepository):
    def create(self, todo_model: TodoModel):
        print('create')

    def delete(self):
        print('delete')

    def update(self):
        print('update')

    def get(self):
        print('get')

    def get_all(self):
        print('get_all')
