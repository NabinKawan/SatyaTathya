from typing import Union
from fastapi import FastAPI, WebSocket
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("accepted")

    while True:
        await websocket.send_text("From API")
        data = await websocket.receive_json()
        print(data)
        
        



