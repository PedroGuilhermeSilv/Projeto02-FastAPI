from app.use_cases.user import UserUseCases
from app.db.models import User as UserModel
from app.schemas.user import User
import pytest
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from datetime import datetime, timedelta
from jose import jwt
from decouple import config


SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

crypt_context = CryptContext(schemes=['sha256_crypt'])

def test_registrer_user(db_session):
    user = User(
        username="Pedro",
        password="pass1",
        isBlocked=True,
        accountId=10,
    )
    uc = UserUseCases(db_session)
    uc.register_user(user=user)

    user_on_db = db_session.query(UserModel).first()

    assert user_on_db is not None
    assert user_on_db.username == user.username
    assert user_on_db.isBlocked == user.isBlocked
    assert crypt_context.verify(user.password, user_on_db.password)

    db_session.delete(user_on_db)
    db_session.commit()


def test_registrer_user_username_already_exist(db_session):
    user_on_db = UserModel(
        username="Pedro",
        password=crypt_context.hash('pass1'),
        isBlocked=True,
        accountId=10
    )
    db_session.add(user_on_db)
    db_session.commit()

    uc = UserUseCases(db_session)
    user = User(
        username="Pedro",
        password=crypt_context.hash('pass1'),
        isBlocked=True,
        accountId=10
    )
    with pytest.raises(HTTPException):
        uc.register_user(user=user)

    db_session.delete(user_on_db)
    db_session.commit()


def test_user_login(db_session, user_on_db):
    uc = UserUseCases(db_session=db_session)

    user = User(
        username=user_on_db.username,
        password='pass2'
    )

    token_data = uc.user_login(user=user, expires_in=30)

    assert token_data.expires_at < datetime.utcnow() + timedelta(32)


def test_user_login_invalid_username(db_session,user_on_db):
    uc = UserUseCases(db_session=db_session)
    user = User(
        username= 'invalid',
        password= 'pass2'
    )

    with pytest.raises(HTTPException):
        token_data = uc.user_login(user=user, expires_in=30)


def test_user_login_invalid_password(db_session,user_on_db):
    uc = UserUseCases(db_session=db_session)
    user = User(
        username= user_on_db.username,
        password= 'invalid'
    )

    with pytest.raises(HTTPException):
        token_data = uc.user_login(user=user, expires_in=30)


def test_verify_token(db_session,user_on_db):
    uc = UserUseCases(db_session=db_session)

    data={
        'sub': user_on_db.username,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }

    acess_token = jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)

    uc.verify_token(token=acess_token)

def test_verify_token_expired(db_session,user_on_db):
    uc = UserUseCases(db_session=db_session)

    data={
        'sub': user_on_db.username,
        'exp': datetime.utcnow() -timedelta(minutes=30)
    }

    acess_token = jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
    with pytest.raises(HTTPException):
        uc.verify_token(token=acess_token)

