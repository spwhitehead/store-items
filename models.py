from pydantic import BaseModel


class Accessories(BaseModel):
    id: int
    name: str
    description: str
    price: float
