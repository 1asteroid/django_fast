from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from .database import session, ENGINE
from webapp.models import Product

session = session(bind=ENGINE)
product_r = APIRouter(prefix="/product")


@product_r.get("/")
async def get_product():
    products = session.query(Product).all()
    context = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "count": product.count,
            "category_id": product.category,
            "add_date": product.create_date,
        }
        for product in products
    ]

    return jsonable_encoder(context)


