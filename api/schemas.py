from pydantic import BaseModel
from typer import Option


class LoginModel(BaseModel):
    username: str
    password: str


class RegisterModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str


class OrderModel(BaseModel):
    product_id: int
    user_id: int
    count: int
    order_status: str


class CategoryModel(BaseModel):
    name: str


class ProductModel(BaseModel):
    name: str
    description: str
    count: int
    price: float


class JWTModel(BaseModel):
    authjwt_secret_key: str = "af53123196a54cb648887f39842e7f4aab35b1dd44e53d95554b83121290580f"