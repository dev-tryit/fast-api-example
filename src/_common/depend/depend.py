from _common.scheme.api_environment import ApiEnvironment
from _common.setting.setting import api_environment
from api.todo.todo_api import TodoApi
from api.todo.todo_api_printer import TodoApiPrinter


def inject_dependency_by_environment(app):
    if api_environment == ApiEnvironment.dev:
        _by_dev(app)
    elif api_environment == ApiEnvironment.qa:
        _by_qa(app)
    elif api_environment == ApiEnvironment.prod:
        _by_qa(app)
    else:
        raise ValueError('unknown api_environment')


def _by_dev(app):
    app.dependency_overrides[TodoApi] = lambda: TodoApiPrinter()
    pass


def _by_qa(app):
    app.dependency_overrides[TodoApi] = lambda: TodoApiPrinter()
    pass


def _by_prod(app):
    app.dependency_overrides[TodoApi] = lambda: TodoApiPrinter()
    pass
