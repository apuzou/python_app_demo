from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

class ShopInfo(BaseModel):
    name: str
    address: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shopinfo: Optional[ShopInfo] = None
    items: List[Item]

app = FastAPI()

# @app.get("/countries/")
# async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
#     return {
#         "country_name": country_name,
#         "country_no": country_no
#     }

@app.post("/")
async def create_item(data: Data):
    return {'data': data}