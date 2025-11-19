from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123 Main St",
    city="Sindi Railway",
    postal_code="12345"
)

user = User(
    id=1,
    name="xitij",
    address=address
)

print(user.model_dump_json())