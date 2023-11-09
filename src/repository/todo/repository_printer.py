from repository.todo.repository import TodoRepository


class TodoRepositoryPrinter(TodoRepository):
    def create(self):
        print('create')

    def delete(self):
        print('delete')

    def update(self):
        print('update')

    def get(self):
        print('get')

    def get_all(self):
        print('get_all')
