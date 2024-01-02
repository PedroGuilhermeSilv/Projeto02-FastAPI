from app.schemas.base import CustombaseModel
from pydantic import field_validator
import re

class Category(CustombaseModel):
    name: str
    slug: str

    @field_validator('slug')
    def validate_slug(cls,value):
        if not re.match('^([a-z]|-|_)+$',value):
            raise ValueError('Invalid slug')
        return value

class CategoryOutput(CustombaseModel):
    id: int
    name: str
    slug: str
    class ConfigDict:
        from_attributes=True


