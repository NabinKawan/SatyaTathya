from app.data.chain_database import redis_db
from app.models.dtos.block_dto import BlockDto
from app.models.enums.data_format_enum import DataFormatEnum
from app.services.db_service import DbService
import json

db = redis_db


class LocalDbService(DbService):

    def add_data(self, block: BlockDto):
        print(block.json())
        db.set(block.block_hash,block.json())

    def get_prev_hash(self):
        pass
        # return db.set[-1].block_hash

    def get_all_datas(self, data_type: DataFormatEnum = DataFormatEnum.BLOCK):
        pass
        # if data_type == DataFormatEnum.BLOCK:
        #     return db.chain_datas
        # elif data_type == DataFormatEnum.JSON:
        #     json_datas = []
        #     for data in db.chain_datas:
        #         json_datas.append(data.dict())
        #     return json_datas
