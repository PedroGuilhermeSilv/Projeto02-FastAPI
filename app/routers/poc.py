from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.routers.deps import get_db_session
from app.schemas.category import CategoryOutput
from app.db.models import Category as CategoryModel
from fastapi_pagination import add_pagination, paginate, Page,LimitOffsetPage, Params, LimitOffsetParams
from fastapi_pagination.ext.sqlalchemy import paginate as sqlalchemy_paginate
from app.use_cases.poc import list_categories_uc

router = APIRouter(prefix='/poc',tags=['POC'])

@router.get('/list', response_model=Page[CategoryOutput])
@router.get('/list-offiset', response_model=LimitOffsetPage[CategoryOutput])
def list_categories(page: int =1, size: int = 50):
    return list_categories_uc(page=page,size=size)

@router.get('/list/sqlalchemy', response_model=Page[CategoryOutput])
@router.get('/list-offiset/sqlalchemy', response_model=LimitOffsetPage[CategoryOutput])
def list_categories(db_session: Session = Depends(get_db_session)):
    categories = db_session.query(CategoryModel)
    return sqlalchemy_paginate(categories)






add_pagination(router)
