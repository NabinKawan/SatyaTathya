from blockchain.data.chain_database import ChainDatabase
from blockchain.dto.block_dto import BlockDto
from blockchain.enums.data_format_enum import DataFormatEnum

db = ChainDatabase()


class DbService:

    @staticmethod
    def add_data(block: BlockDto):
        db.chain_datas.append(block)

    @staticmethod
    def get_prev_hash(is_genesis: bool = False):
        if is_genesis:
            return 'sakdfhjasdf'
        return db.chain_datas[-1].prev_hash

    @staticmethod
    def get_all_datas(type: DataFormatEnum = DataFormatEnum.BLOCK):
        if type == DataFormatEnum.BLOCK:
            return db.chain_datas
        elif type == DataFormatEnum.JSON:
            json_datas = []
            for data in db.chain_datas:
                json_datas.append(data.dict())
            return json_datas
