from fastapi import APIRouter, Body, Depends

from _common.exception.api_exception import ApiException
from domain.self_management.scheme.request.todo_create_reqeust import TodoCreateRequest
from domain.self_management.service import SelfManagementService

router = APIRouter()


@router.post('/todo', status_code=201)
def create_todo(
        request: TodoCreateRequest,
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        response = service.create_todo(request.to_vo())
        return response
    except ApiException as e:
        raise e


@router.get('/todos', status_code=200)
def get_todos(
        order: str | None = None,
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        response = service.get_todos(order)
        return response
    except ApiException as e:
        raise e


@router.get('/todos/{todo_id}', status_code=200)
def get_todo(
        todo_id: int,
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        response = service.get_todo(todo_id)
        return response
    except ApiException as e:
        raise e


@router.patch('/todos/{todo_id}', status_code=200)
def update_todo(
        todo_id: int,
        is_done: bool = Body(embed=True),
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        response = service.update_todo(todo_id, is_done)
        return response
    except ApiException as e:
        raise e


@router.delete('/todos/{todo_id}', status_code=204)
def delete_todo(
        todo_id: int,
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        response = service.delete_todo(todo_id)
        return response
    except ApiException as e:
        raise e
