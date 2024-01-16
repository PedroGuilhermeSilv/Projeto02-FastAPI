from app.schemas.people import People
from app.schemas.user import User
import pytest

def test_people_schema():
    user = User(
        username='pedro',
        password='pass',
        is_blocked=True,
        account_id=10
    )
    people = People(
        name='Lucas',
        cpf = '61497437355',
        organization = 20,
        role = 'cargo',
        account_id= 10,
        email='pedro@hotmail.com',
        ranking=9,
        description='descrição',
        birthday= 'aniversario',
        avatar='avatar',
        owner_user= user
    )
    assert people.dict() == {
        'name': 'Lucas',
        'cpf':'61497437355',
        'organization':20,
        'role':'cargo',
        'account_id':10,
        'email': 'pedro@hotmail.com',
        'ranking': 9,
        'description':'descrição',
        'birthday': 'aniversario',
        'avatar': 'avatar',
        'owner_user':{
            'username': 'pedro',
            'password': 'pass',
           'is_blocked': True,
           'account_id': 10

        }

    }

