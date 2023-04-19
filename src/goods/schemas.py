from pydantic import BaseModel


class RequestIdSchema(BaseModel):
    product_id: int


example_200_response = {
    'nm_id': 139760663,
    'name': 'iPhone 14 Pro Max',
    'brand': 'Apple',
    'brand_id': 6049,
    'site_brand_id': 16049,
    'supplier_id': 887491,
    'sale': 26,
    'price': 199990,
    'sale_price': 147992,
    'rating': 4,
    'feedbacks': 7,
    'colors': 'серый'
}


class Product(BaseModel):
    nm_id: int
    name: str
    brand: str
    brand_id: int
    site_brand_id: int
    supplier_id: int
    sale: int
    price: int
    sale_price: int
    rating: int
    feedbacks: int
    colors: str = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": example_200_response
        }
