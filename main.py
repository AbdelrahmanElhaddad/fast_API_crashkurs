from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel, Field
from jose import jwt
from enum import Enum


items = [
    {"name": "Computer", "preis": 2000, "typ": "hardware"},
    {"name": "Computer", "preis": 4000, "typ": "hardware"},
    {"name": "Computer", "preis": 3000, "typ": "hardware"},
    {"name": "Monitor", "preis": 1000, "typ": "hardware"},
    {"name": "Windows", "preis": 300, "typ": "software"},
    {"name": "COD:BO2", "preis": 30, "typ": "software"},
]

class Type(Enum):
    hardware = "hardware"
    software = "software"

class Item(BaseModel):
    name: str
    preis: int = Field(100, gt=50, lt=10000)
    typ: Type

class ResponseItem(BaseModel):
    name: str
    typ: Type

app = FastAPI()

@app.get('/')
async def get_root():
    return "Hello, world!"

@app.get('/items/')
async def get_all_items():
    return items


@app.get('/items/{items_id}')
async def get_item(items_id: int):
    return items[items_id]

@app.get('/items/computers/')
async def get_computers():
    output = []
    for item in items:
        if item["name"] == "Computer":
            output.append(item)

    return output

@app.post('/items/', response_model=ResponseItem)
async def add_item(data: Item):
    items.append(data)
    return data

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    del items[item_id]
    
