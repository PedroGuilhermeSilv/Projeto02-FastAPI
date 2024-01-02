from app.schemas.base import CustombaseModel
from pydantic import field_validator
import re
from datetime import datetime


class User(CustombaseModel):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls,value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$',value):
            raise ValueError('Invalid username')
        return value
    

class TokenData(CustombaseModel):
    acess_token: str
    expires_at: datetime

