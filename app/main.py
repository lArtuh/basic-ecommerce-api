from fastapi import FastAPI
from app.routers import products, categories, orders
from app.database import engine
from app.models import Base

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Basic E-commerce API is running"}
  
Base.metadata.create_all(bind=engine)

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(categories.router, prefix="/categories",
                   tags=["Categories"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
