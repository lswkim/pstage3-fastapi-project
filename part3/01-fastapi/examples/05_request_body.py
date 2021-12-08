from typing import Optional
from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# FastAPI 객체 생성
app = FastAPI()

# "/" 로 접근하면 return 을 보여줌
@app.get("/")
def read_root():
    return {"Hello": "World"}

# path parameter 확인하기
@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}

# query parameter 확인하기
@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# optional parameter 확인하기
@app.get("/items/{item_id}")
def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id}

# post method 사용
@app.post("/items/")
def create_item(item: Item):
    return item

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)