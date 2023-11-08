from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from _common.connection.mysql_connection import get_session
from api.todo.api import TodoApi
from api.todo.scheme.todo_model import ToDoModel


class TodoApiMySql(TodoApi):
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self):
        print('create')

    def delete(self):
        print('delete')

    def update(self):
        print('update')

    def get(self):
        print('get')

    def get_all(self) -> List[ToDoModel]:
        return list(self.session.scalars(select(ToDoModel)))
