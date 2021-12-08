from fastapi import FastAPI
import uvicorn

# FastAPI 객체 생성
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

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

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)