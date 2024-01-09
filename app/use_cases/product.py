from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi.exceptions import HTTPException
from fastapi import status
from app.db.models import Product as ProductModel
from app.db.models import Category as CategoryModel
from app.schemas.product import Product, ProductOutput
from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate



class ProductUseCases:
    def __init__(self,db_session: Session):
        self.db_session = db_session
    def add_product(self, product: Product, category_slug: str):
        category = self.db_session.query(CategoryModel).filter_by(slug=category_slug).first()
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'category: {category_slug} is not existe ')
        product_model = ProductModel(name=product.name,
                                     slug=product.slug,
                                     stock=product.stock,
                                     price=product.price,
                                     category_id=category.id
                                     )

        self.db_session.add(product_model)
        self.db_session.commit()  
    def update_product(self, id: int,product: Product):
        product_on_db = self.db_session.query(ProductModel).filter_by(id=id).first()
        if not product_on_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'product: {id} is not existe ')
        product_on_db.name = product.name
        product_on_db.slug = product.slug
        product_on_db.price = product.price
        product_on_db.stock = product.stock

        self.db_session.add(product_on_db)
        self.db_session.commit()  
    
    def delete_product(self,id:int):
        product_on_db = self.db_session.query(ProductModel).filter_by(id=id).first()
        if  product_on_db is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not exist")
        self.db_session.delete(product_on_db)
        self.db_session.commit()
    
    def list_products(self, page: int=1, size: int=50 ,search :str =''):
        products_ond_db = self.db_session.query(ProductModel).filter(
            or_(
                ProductModel.name.ilike(f'%{search}%'),
                ProductModel.slug.ilike(f'%{search}%'),
            )
        )
        params = Params(page=page,size=size)
        page = paginate(products_ond_db,params=params)

        return page   

    def _serialize_product(self, product_on_db: ProductModel):
        product_dict = {'id':product_on_db.id,
                        'name':product_on_db.name,
                        'slug':product_on_db.slug,  
                        'price':product_on_db.price,
                        'stock': product_on_db.stock,
                        'category':{
                            'name': product_on_db.category.name,
                            'slug':product_on_db.category.slug
                        }}
        
        return ProductOutput(**product_dict)

      
        
