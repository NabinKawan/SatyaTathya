from fastapi import FastAPI,Request,HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()    


class Voters(BaseModel):
    # id:Optional[int]=None
    username:str
    password:str
    balance:int

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def show_users(db:Session=Depends(get_db)):
    return db.query(models.User).all()

@app.post("/api/login/")
async def login(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    user = db.query(models.User).filter(models.User.username == data["username"], models.User.password == data["password"]).first()
    if user:
        return {"message": "Success"}
    else:
        return {"message": "Invalid username or password"}


@app.post("/api/register/")
def register(username: str, password: str,balance:str, db: Session = Depends(get_db)):
    user = models.User(username=username, password=password,balance=balance)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Success"}





    