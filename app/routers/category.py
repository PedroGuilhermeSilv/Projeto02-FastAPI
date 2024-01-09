from fastapi import APIRouter, Depends , status, Response
from app.schemas.category import Category , CategoryOutput
from app.routers.deps import get_db_session, auth
from app.db.connection import Session
from app.use_cases.category import CategoryUseCases
from typing import List
from fastapi_pagination import Page
from fastapi import Query

router = APIRouter(prefix='/category', tags=['Category'], dependencies=[Depends(auth)])

@router.post('/add', status_code=status.HTTP_201_CREATED, description="Add new category")
def add_category(
    category: Category,
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session=db_session)
    uc.add_category(category=category)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/list',response_model=Page[CategoryOutput],description="Page ")
def list_categories(
    size: int =Query(1,ge=1,description="Page number"),
    page:int =Query(50,ge=1, le=100,description="Page size"),
    db_session: Session = Depends(get_db_session)):
    uc = CategoryUseCases(db_session=db_session)
    response = uc.list_categories(page=page,size=size)
    return response

@router.delete('/{id}', description="Delete category")
def delete_category(id:int,db_session: Session = Depends(get_db_session)):
    uc = CategoryUseCases(db_session=db_session)
    uc.delete_category(id=id)

    return Response(status_code=status.HTTP_200_OK)

    