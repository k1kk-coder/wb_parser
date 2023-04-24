from pydantic import BaseModel


class RequestIdSchema(BaseModel):
    product_id: int


example_response = {
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
            "example": example_response
        }


product_not_found_response_404 = {
    "description": "Not Found",
    "content": {
        "application/json": {
            "example": {
                "detail": "PRODUCT_WITH_THIS_ID_WAS_NOT_FOUND"}
        }
    }
}

successful_response_200 = {
    'description': 'Successful Response',
    'content': {
        'application/json': {
            "example": example_response
        }
    }
}

already_exists_response_409 = {
    'description': 'Conflict',
    'content': {
        'application/json': {
            'example': {
                'detail': 'THIS_PRODUCT_IS_ALREADY_IN_THE_DATABASE'}
        }
    }
}

forbidden_response_400 = {
    'description': 'Bad Request',
    'content': {
        'application/json': {
            'example': {
                'detail': 'INVALID_PRODUCT_ID'}
        }
    }
}
