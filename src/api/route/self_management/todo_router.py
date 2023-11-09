from fastapi import APIRouter, Body, Depends

from _common.exception.my_api_exception import MyApiException
from domain.self_management.scheme.request.todo_create_reqeust import TodoCreateRequest
from domain.self_management.service import SelfManagementService

# TODO: from pydantic import BaseSettings -> env
# TODO: fastapi-users

router = APIRouter()


@router.get('/', status_code=200)
def get_todos(
        order: str | None = None,
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        result = service.get_todos(order)
        # TODO: result to response
        return result
    except MyApiException as e:
        raise e


@router.get('/{todo_id}', status_code=200)
def get_todo(
        todo_id: int,
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        result = service.get_todo(todo_id)
        # TODO: result to response
        return result
    except MyApiException as e:
        raise e


@router.post('/', status_code=201)
def create_todo(
        request: TodoCreateRequest,
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        result = service.create_todo(request.to_vo())
        # TODO: result to response
        return result
    except MyApiException as e:
        raise e


@router.put('/{todo_id}', status_code=200)
def update_todo(
        todo_id: int,
        is_done: bool = Body(embed=True),
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        result = service.update_todo(todo_id, is_done)
        # TODO: result to response
        return result
    except MyApiException as e:
        raise e


@router.delete('/{todo_id}', status_code=204)
def delete_todo(
        todo_id: int,
        service: SelfManagementService = Depends(),
):
    try:
        # TODO: validate
        result = service.delete_todo(todo_id)
        # TODO: result to response
        return result
    except MyApiException as e:
        raise e
