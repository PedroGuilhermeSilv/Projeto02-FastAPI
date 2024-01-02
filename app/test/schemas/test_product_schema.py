from app.schemas.product import Product, ProductInput, ProductOutput
import pytest
from app.schemas.category import Category


def test_product_schema():
    product = Product(
        name='Roupa',
        slug='roupa',
        price = 10.0,
        stock = 2
    )
    assert product.dict()=={
        'name':'Roupa',
        'slug':'roupa',
        'price': 10.0,
        'stock':2
    }
def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        prodcut = Product(
            name='Roupa',
            slug='roupa de cama',
            price= 10.0,
            stock=2
        )
    with pytest.raises(ValueError):
        product = Product(
            name='Roupa',
            slug='cão',
            price= 10.0,
            stock=2
        )
    with pytest.raises(ValueError):
        product = Product(
            name='Roupa',
            slug='Roupa',
            price= 10.0,
            stock=2
        )

def test_product_schema_price():
    with pytest.raises(ValueError):
        product = Product(
            name='Roupa',
            slug='roupa',
            price= 0,
            stock=2
        )

def test_product_input_schema():
    product = Product(
        name='Roupa',
        slug='roupa',
        price = 10.0,
        stock = 2
    )
    productinput = ProductInput(
        category_slug="roupa",
        product= product
    )

    assert productinput.dict()=={
        "category_slug":"roupa",
        "product":{
            "name": "Roupa",
            "slug":'roupa',
            "price": 10.0,
            "stock": 2
        }
    }
def test_product_output_schema():
    category = Category(name="Roupa",slug="roupa")
    product_output = ProductOutput(
        id=1,
        name='Camiseta',
        slug='camiseta',
        price = 10.0,
        stock = 2,
        category=category
    )

    assert product_output.dict() =={
        'id':1,
        'name': 'Camiseta',
        'slug': 'camiseta',
        'price': 10.0,
        'stock':2,
        'category':{
            'name':'Roupa',
            'slug':'roupa'
        }
    }