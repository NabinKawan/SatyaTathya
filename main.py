from app.models.enums.data_format_enum import DataFormatEnum
from app.services.impl.khwopa_service import KhwopaService
from app.services import db_service


def main() -> None:
    khwopa_service = KhwopaService()
    khwopa_service.init_genesis_block()
    khwopa_service.add_block('ram to shyam :3 btc')
    khwopa_service.add_block("sita to gita: 2 btc")
    khwopa_service.add_block("hari to harry: 2 btc")

    default_datas = db_service.get_all_datas()
    print(default_datas)
    json_datas = db_service.get_all_datas(data_type=DataFormatEnum.JSON)
    print(json_datas )
    print("\n")

if __name__ == '__main__':
    main()


import asyncio
import json
import websockets

async def hello():
    json_datas = db_service.get_all_datas(data_type=DataFormatEnum.JSON)
    # print(type(json_datas))

    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        print(await websocket.recv()) 
        # await websocket.send(bytes(str(json_datas),"utf-8"))
        await websocket.send(json.dumps(json_datas))
        print(type(json.dumps(json_datas)))
        print(type(json.loads(json.dumps(json_datas))))

asyncio.run(hello())  



