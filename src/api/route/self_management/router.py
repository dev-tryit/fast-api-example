from datetime import datetime

from fastapi import APIRouter, Body, Depends

from _common.scheme.response.my_response import MyResponse
from api.route.self_management.scheme.request.review_create_reqeust import ReviewCreateRequest
from api.route.self_management.scheme.request.todo_create_reqeust import TodoCreateRequest
from domain.self_management.service import SelfManagementService

# TODO: from pydantic import BaseSettings -> env
# TODO: fastapi-users

router = APIRouter()

# TODO: python test 쪽에 di 하는 decorator가 있다. 참고 필요.
# SelfManagementService를 Depends() 형식으로 만드는게 효율적인가? 싱글톤으로 하고, factory pattern으로 구현체를 바꿀 수 있는게 좋아보임.


'''--------------------'''
'''--------------todo'''
'''--------------------'''


@router.get('/todo/', status_code=200)
def get_todos(
        order: str | None = None,
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = service.get_todos(order)
    return MyResponse(result=result)


@router.get('/todo/{todo_id}', status_code=200)
def get_todo(
        todo_id: int,
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = service.get_todo(todo_id)
    return MyResponse(result=result)


@router.post('/todo/', status_code=201)
def create_todo(
        request: TodoCreateRequest,
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = service.create_todo(request.to_vo())
    return MyResponse(result=result)


@router.patch('/todo/{todo_id}', status_code=200)
def update_todo(
        todo_id: int,
        is_done: bool = Body(embed=True),
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = service.update_todo(todo_id, is_done)
    return MyResponse(result=result is not None)


@router.delete('/todo/{todo_id}', status_code=200)
def delete_todo(
        todo_id: int,
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = service.delete_todo(todo_id)
    return MyResponse(result=result is not None)


'''--------------------'''
'''--------------review'''
'''--------------------'''


@router.get('/review/', status_code=200)
async def get_reviews(
        order: str | None = None,
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = await service.get_reviews(order)
    return MyResponse(result=result)


@router.get('/review/{review_id}', status_code=200)
async def get_review(
        review_id: str,
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = await service.get_review(review_id)
    return MyResponse(result=result)


@router.post('/review/', status_code=201)
async def create_review(
        request: ReviewCreateRequest,
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = await service.create_review(request.to_vo())
    return MyResponse(result=result)


@router.patch('/review/{review_id}', status_code=200)
async def update_review(
        review_id: str,
        name: str | None = Body(embed=True),
        product: str | None = Body(embed=True),
        rating: float | None = Body(embed=True),
        review: str | None = Body(embed=True),
        date: datetime | None = Body(embed=True),
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = await service.update_review(review_id, name, product, rating, review, date)
    return MyResponse(result=result is not None)


@router.delete('/review/{review_id}', status_code=200)
async def delete_review(
        review_id: str,
        service: SelfManagementService = Depends(),
):
    # TODO: validate
    result = await service.delete_review(review_id)
    return MyResponse(result=result is not None)
