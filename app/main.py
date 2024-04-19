from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    nationality: Optional[str] = None
    favorite_list: list[str]

class returnUsr(BaseModel): 
    name: str
    age: int
    favorite: str
    
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def home_post(body: User): #Json 형식으로 들어오면 알아서 변환해준다
    return returnUsr(name= body.name, age= body.age+10, favorite=body.favorite_list[0])