from sqlalchemy import Column, Integer, String , ForeignKey, DateTime, Float, func, Boolean
from app.db.base import Base
from sqlalchemy.orm import relationship



class Category(Base):
    __tablename__ = 'categories'
    id = Column('id',Integer, primary_key=True,autoincrement=True)
    name = Column('name',String,nullable=False)
    slug = Column('slug',String,nullable=False)
    products = relationship('Product', back_populates='category')

class Product(Base):
    __tablename__ = 'products'
    id = Column('id',Integer, primary_key=True,autoincrement=True)
    name = Column('name',String,nullable=False)
    slug = Column('slug',String,nullable=False)
    price = Column('price',Float)
    stock = Column('stock',Integer)
    created_at = Column('created_at',DateTime, default=func.now())
    updated_at = Column('updated_at',DateTime, onupdate=func.now())
    category_id = Column('category_id',ForeignKey('categories.id'), nullable=False)
    category = relationship('Category',back_populates='products')

class User(Base):
    __tablename__ = 'users'
    id = Column('id',Integer, primary_key=True,autoincrement=True) 
    username = Column('username',String,unique=True,nullable=False)
    password = Column('password',String,nullable=False) 
    accountId = Column('account_id',Integer,nullable=True)
    isBlocked = Column('is_blocked',Boolean,default=True)
    created_at = Column('created_at',DateTime, default=func.now())



