from app.data.chain_database import redis_db
from app.models.dtos.block_dto import BlockDto
from app.models.enums.data_format_enum import DataFormatEnum
from app.services.db_service import DbService
import json

db = redis_db


class LocalDbService(DbService):

    def add_data(self, block: BlockDto):
        db.rpush('block:tracks', block.block_hash)
        db.set(block.block_hash, block.json())
        print(f'Successfully minted {block.block_hash}: {block.json()}')
        return block.block_hash

    def get_prev_hash(self):
        return db.lrange('block:tracks', -1, -1)[0]

    def get_all_datas(self, data_type: DataFormatEnum = DataFormatEnum.BLOCK):
        block_tracks = db.lrange('block:tracks', 0, -1)

        def get_block(block_hash: str):
            block_json = json.loads(db.get(block_hash))
            if (data_type == DataFormatEnum.BLOCK):
                return BlockDto(**block_json)
            elif (data_type == DataFormatEnum.JSON):
                return block_json

        return list(map(get_block, block_tracks))

    def get_data_by_identifier(self, block_hash: str, data_type: DataFormatEnum = DataFormatEnum.BLOCK):
        data = db.get(block_hash)
        if (data):
            block_json = json.loads(db.get(block_hash))
            if (data_type == DataFormatEnum.BLOCK):
                return BlockDto(**block_json)
            elif (data_type == DataFormatEnum.JSON):
                return block_json

    def update_contract_data(self, contract_address: str, contract_data: str):
        block_json = json.loads(db.get(contract_address))
        block_json['contract_data'] = contract_data
        db.set(contract_address, json.dumps(block_json))
        print(f'Successfully updated contract {contract_address}: {block_json}')
