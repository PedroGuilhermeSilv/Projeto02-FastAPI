from app.schemas.base import CustombaseModel
from app.schemas.user import User
from pydantic import field_validator
import re

class People(CustombaseModel):
    name: str
    cpf: str
    organization: int
    role: str
    account_id: int
    email: str
    ranking: int
    description: str
    birthday: str
    avatar: str
    owner_user: User




