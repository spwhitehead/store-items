from pydantic import BaseModel


class Accessory(BaseModel):
    id: int
    name: str
    description: str
    price: float
