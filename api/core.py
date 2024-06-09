# from fastapi import FastAPI, security, HTTPException
#
# from .database import session, ENGINE
# from .order_router import order_r
# from .product_router import product_r
#
#
# app = FastAPI()
# app.include_router(order_r, prefix="/fastapi/v1")
# app.include_router(product_r, prefix="/fastapi/v1")
#
#
# @app.get("/fastapi/v1")
# async def landing():
#     return {"message": "hey this is landing page"}


from product_router import product_r

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

fastapi_app = FastAPI()

# routers
fastapi_app.include_router(product_r, tags=["product"], prefix="/api/v1/product")

# to mount Django