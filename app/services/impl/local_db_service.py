from app.data.chain_database import ChainDatabase
from app.models.dtos.block_dto import BlockDto
from app.models.enums.data_format_enum import DataFormatEnum
from app.services.db_service import DbService

db = ChainDatabase()


class LocalDbService(DbService):

    def add_data(self, block: BlockDto):
        db.chain_datas.append(block)

    def get_prev_hash(self):
        return db.chain_datas[-1].block_hash

    def get_all_datas(self, data_type: DataFormatEnum = DataFormatEnum.BLOCK):
        if data_type == DataFormatEnum.BLOCK:
            return db.chain_datas
        elif data_type == DataFormatEnum.JSON:
            json_datas = []
            for data in db.chain_datas:
                json_datas.append(data.dict())
            return json_datas
