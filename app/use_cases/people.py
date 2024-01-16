from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from app.db.models import People as PeopleModel
from app.schemas import People


# ainda a fazer
class PeopleUseCases:
    def __init__(self,db_session: Session):
        self.db_session = db_session
    def register_people(self,people:People):
        people_on_db = PeopleModel(
            username=user.username,
            password=crypt_context.hash(user.password),
            is_blocked=user.is_blocked,
            account_id=user.account_id,
            
        )

        self.db_session.add(people_on_db)
        
