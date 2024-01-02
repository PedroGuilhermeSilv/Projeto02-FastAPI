from app.schemas.user import User, TokenData
import pytest
from datetime import datetime, timedelta
from app.use_cases.user import UserUseCases
from fastapi.exceptions import HTTPException



def test_user_schema():
    user = User(
        username='pedro',
        password='pass'
    )

    assert user.dict() == {
        'username': 'pedro',
        'password':'pass'
    }

def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(
        username='joão#',
        password='pass'
    )
        
def test_token_data():
    expires_at = datetime.now()
    token_data = TokenData(
        acess_token="token",
        expires_at=expires_at
    )

    assert token_data.dict() =={
        'acess_token': 'token',
        'expires_at': expires_at
    }





