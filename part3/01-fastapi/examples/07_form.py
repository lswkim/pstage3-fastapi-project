from fastapi import FastAPI, Form, Request
from fastapi import templating
from fastapi.templating import Jinja2Templates
import uvicorn

# FastAPI 객체 생성
app = FastAPI()
templates = Jinja2Templates(directory='./')

# "/" 로 접근하면 return 을 보여줌
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/login/")
def get_login_form(request: Request):
    return templates.TemplateResponse('login_form.html', context={'request': request})

@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username", username}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)