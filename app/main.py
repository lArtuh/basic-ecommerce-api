from fastapi import FastAPI
from app.routers import products, categories, orders
from app.database import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(categories.router, prefix="/categories",
                   tags=["Categories"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
