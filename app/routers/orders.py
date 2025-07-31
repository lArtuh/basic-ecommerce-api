from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)


@router.get("/", response_model=list[schemas.Order])
def list_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)
