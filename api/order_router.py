from fastapi import APIRouter

order_r = APIRouter(prefix="/order")


@order_r.get("/")
async def get_order():
    return {"message": "This is order page"}

