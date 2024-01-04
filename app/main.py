from fastapi import FastAPI 
from app.routers.category import router as category_route
from app.routers.product import router as product_route
from app.routers.user import router as user_route
from app.routers.poc import router as poc_route


app = FastAPI()
app.include_router(category_route)
app.include_router(product_route)
app.include_router(user_route)
app.include_router(poc_route)

@app.get('/')
def health_check():
    return "Hello, Word"