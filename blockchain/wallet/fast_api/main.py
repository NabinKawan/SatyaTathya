from fastapi import FastAPI,Request,HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
# from models import Card

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
@app.post("/api/cards")
async def create_card(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    try:
        card = models.Card(sender_name=data["Senders_name"], receiver_name=data["Receivers_name"], balance=data["balance"])
        db.add(card)
        db.commit()
        return {"message": "Card created successfully"}
    except Exception as e:
        return {"message": "An error occurred: {}".format(str(e))}


@app.get("/api/get_cards")
def get_all_cards(db:Session=Depends(get_db)):
    cards = db.query(models.Card).all()
    return cards

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


@app.post("/api/transfer")
async def transfer_balance(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    sender_wallet_id = data["sender_wallet_id"]
    receiver_wallet_id = data["receiver_wallet_id"]
    amount =int(data["amount"])
    sender = db.query(models.User).filter(models.User.username == sender_wallet_id).first()
    receiver = db.query(models.User).filter(models.User.username == receiver_wallet_id).first()
    if sender and receiver:
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            db.add(sender)
            db.add(receiver)
            db.commit()
            return {"message": "Transfer successful"}
        else:
            return HTTPException(status_code=400, detail="Insufficient balance")
    else:
        return HTTPException(status_code=400, detail="Invalid wallet id")


@app.post("/api/register/")
def register(username: str, password: str,balance:str, db: Session = Depends(get_db)):
    user = models.User(username=username, password=password,balance=balance)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Success"}





    