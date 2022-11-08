from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.exceptions import HTTPException as StarletteHTTPException


from .schemas import UserOut, UserIn

from . import crud

router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@router.get('', response_model=list[UserOut])
def list_users() -> list[UserOut]:
    return crud.get_users()


@router.post(
    '',
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user_in: UserIn) -> UserOut:
    return crud.create_user(user_in)


@router.get('/{user_id}', response_model=UserOut)
def get_user(user_id: int) -> UserOut | None:
    user = crud.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} doesn't exist!"
    )


@router.delete(
    '/{user_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(user_id: int):
    crud.delete_user(user_id)
