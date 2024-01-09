from app.schemas.base import CustombaseModel
from pydantic import field_validator
import re
from datetime import datetime
from app.schemas.category import CategoryOutput

class Product(CustombaseModel):
    name: str
    slug: str
    price: float
    stock: int

    @field_validator('slug')
    def validate_slug(cls,value):
        if not re.match('^([a-z]|-|_)+$',value):
            raise ValueError('Invalid slug')
        return value
    @field_validator('price')
    def validate_price(cls,value):
        if value <= 0:
            raise ValueError('Invalid price')
        return value

class ProductOutput(Product):
    id: int
    category: CategoryOutput
    class ConfigDict:
        from_attributes=True


class ProductInput(CustombaseModel):
    category_slug: str
    product: Product




