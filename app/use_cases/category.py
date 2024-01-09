from app.db.models import Category as CategoryModel
from app.schemas.category import Category , CategoryOutput
from sqlalchemy.orm import Session 
from fastapi.exceptions import HTTPException
from fastapi import status
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Params
from sqlalchemy import Select


class CategoryUseCases:
    def __init__(self,db_session: Session):
        self.db_session = db_session
    def add_category(self, category: Category):
        category_model = CategoryModel(
            name = category.name,
            slug=category.slug
        )
        self.db_session.add(category_model)
        self.db_session.commit()

    def list_categories(self,page: int =1, size: int =50):
        categories_on_db = self.db_session.query(CategoryModel)
        params = Params(page=page , size=size)
        return paginate(categories_on_db,params=params)
        
    
    def delete_category(self, id: int):
        category_model = self.db_session.query(CategoryModel).filter_by(id=id).first()
        if not category_model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not exist")
        self.db_session.delete(category_model)
        self.db_session.commit()

    
    def serializer_category(self,category_model: CategoryModel):
        return CategoryOutput(id=category_model.id, name=category_model.name,slug= category_model.slug)
