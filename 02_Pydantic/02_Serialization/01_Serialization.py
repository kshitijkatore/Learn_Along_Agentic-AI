from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: str
    name: str
    email: str
    is_active: bool = True
    createAt: datetime
    address: Address
    tags: List[str] = []


    model_config = ConfigDict(
        json_encoders ={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name="Xitij",
    email="xitij@gmail.com",
    createAt=datetime(2025, 3, 15, 14, 30),
    address=Address(
            street="Something",
            city="Sindi",
            zip_code="34343"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
    )


user_dict =user.model_dump()
print(user_dict)