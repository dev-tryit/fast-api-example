from fastapi import Depends
from sqlalchemy.orm import Session

from _common.database.mysql_connection import get_db
from api.todo.todo_api import TodoApi


class TodoApiMySql(TodoApi):
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

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
