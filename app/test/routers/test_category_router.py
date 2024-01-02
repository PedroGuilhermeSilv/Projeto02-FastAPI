from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app.db.models import Category as CategoryModel

client = TestClient(app)
headers = {"Authorization": "Bearer token"}
client.headers = headers

def test_add_category_route(db_session):
    body ={
        "name": "Roupa",
        "slug": "roupa"
    }
    response = client.post('/category/add',json=body)

    assert response.status_code == status.HTTP_201_CREATED

    categories_on_db = db_session.query(CategoryModel).all()

    assert len(categories_on_db) == 1
    db_session.delete(categories_on_db[0])
    db_session.commit()

def test_list_category_route(categories_on_db):

    response = client.get('/category/list')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data[0] == {
        "name": categories_on_db[0].name,
        "slug": categories_on_db[0].slug,
        "id": categories_on_db[0].id
    }

def test_delete_category_route(db_session):
    category_model = CategoryModel(name="Ropupa", slug="roupa")
    db_session.add(category_model)
    db_session.commit()

    response = client.delete(f'/category/{category_model.id}')
    category_model = db_session.query(CategoryModel).first()

    assert response.status_code == status.HTTP_200_OK
    assert category_model is None
    

