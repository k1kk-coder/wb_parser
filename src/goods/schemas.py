from pydantic import BaseModel


class RequestIdSchema(BaseModel):
    product_id: int
