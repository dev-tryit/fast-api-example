from _common.scheme.my_environment import MyEnvironment
from _common.setting.setting import my_environment
from api.todo.todo_api import TodoApi
from api.todo.todo_api_mysql import TodoApiMySql


def inject_dependency_by_environment(app):
    if my_environment == MyEnvironment.dev:
        _by_dev(app)
    elif my_environment == MyEnvironment.qa:
        _by_qa(app)
    elif my_environment == MyEnvironment.prod:
        _by_qa(app)
    else:
        raise ValueError('unknown api_environment')


def _by_dev(app):
    app.dependency_overrides[TodoApi] = lambda: TodoApiMySql()
    pass


def _by_qa(app):
    app.dependency_overrides[TodoApi] = lambda: TodoApiMySql()
    pass


def _by_prod(app):
    app.dependency_overrides[TodoApi] = lambda: TodoApiMySql()
    pass
