from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app.db.models import Category as CategoryModel
from app.db.models import Product as ProductModel

client = TestClient(app)
headers = {"Authorization": "Bearer token"}
client.headers = headers

def test_add_product_route(db_session,categories_on_db):
    body ={
        "product":{
            "name": "Roupa",
            "slug": "roupa",
            "price": 22.2,
            "stock": 10
        },
        "category_slug": categories_on_db[0].slug
    }
    response = client.post('/product/add',json=body)

    assert response.status_code == status.HTTP_201_CREATED

    product_on_db = db_session.query(ProductModel).all()
    
    assert len(product_on_db) ==1

    db_session.delete(product_on_db[0])
    db_session.commit()

def test_add_product_route_invalid_category(db_session):
    body ={
        "category_slug": 'invalid',
        "product":{
            "name": "Roupa",
            "slug": "roupa",
            "price": 22.2,
            "stock": 10
        }
        
    }
    response = client.post('/product/add',json=body)

    assert response.status_code == status.HTTP_404_NOT_FOUND

    product_on_db = db_session.query(ProductModel).all()
    
    assert len(product_on_db) ==0

def test_update_product_route(db_session,product_on_db):
    body ={
            "name": "Update",
            "slug": "update",
            "price": 22.2,
            "stock": 10

    }
    response = client.put(f'/product/update/{product_on_db.id}',json=body)

    assert response.status_code == status.HTTP_200_OK

    db_session.refresh(product_on_db)
    product_on_db.name == 'Update'
    product_on_db.slug == 'update'
    product_on_db.price == 22.2
    product_on_db.stock == 10

def test_update_product_route_id_invalid():
    body ={
            "name": "Update",
            "slug": "update",
            "price": 22.2,
            "stock": 10

    }
    response = client.put('/product/update/1',json=body)

    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_product_route(db_session,product_on_db):

    response = client.delete(f'/product/delete/{product_on_db.id}')

    assert response.status_code == status.HTTP_200_OK

    product_on_db = db_session.query(ProductModel).all()

    assert len(product_on_db) ==0

def test_delete_product_route_id_invalid(db_session):

    response = client.delete(f'/product/delete/1')

    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_list_products_route(products_on_db):
    response = client.get('/product/list?page=1&size=2')

    data = response.json()

    assert 'items' in data
    assert len(data['items']) == 2

    assert data['items'][0] == {
        'id':products_on_db[0].id,
        'name':products_on_db[0].name,
        'slug':products_on_db[0].slug,
        'price':products_on_db[0].price,
        'stock':products_on_db[0].stock,
        'category':{
            "id" : products_on_db[0].category_id,
            'name':products_on_db[0].category.name,
            'slug':products_on_db[0].category.slug
        }
    }

    assert data['total'] == 3
    assert data['page'] == 1
    assert data['size'] == 2
    assert data['pages'] == 2


def test_list_products_search_route(products_on_db):
    response = client.get('/product/list?search=mike')

    data = response.json()

    assert 'items' in data

    assert len(data['items']) == 3

    assert data[0] == {
        'id':products_on_db[0].id,
        'name':products_on_db[0].name,
        'slug':products_on_db[0].slug,
        'price':products_on_db[0].price,
        'stock':products_on_db[0].stock,
        'category':{
            "id" : products_on_db[0].category_id,
            'name':products_on_db[0].category.name,
            'slug':products_on_db[0].category.slug
        }
    }

    assert data['total'] == 3
    assert data['page'] == 1
    assert data['size'] == 50
    assert data['pages'] == 1







