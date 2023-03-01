import json

from app.components.block.impl.genesis_block import GenesisBlock
from app.components.block.impl.normal_block import NormalBlock
from app.models.dtos.block_dto import BlockDto, NormalTxDto, ContractTxDto
from app.services.blockchain_service import BlockchainService
from pydantic import Json
from app.services import db_service
from typing import Any


class KhwopaService(BlockchainService):

    def add_block(self, tx: str):
        tx = NormalTxDto(metadata=tx)
        block = NormalBlock(tx)
        return db_service.add_data(BlockDto(block_hash=block.block_hash,
                                            prev_hash=block.prev_hash, timestamp=block.timestamp, tx=block.tx))

    def add_contract(self, byte_code: str, contract_data):
        tx = ContractTxDto(byte_code=byte_code, contract_data=contract_data)
        block = NormalBlock(tx)
        return db_service.add_data(BlockDto(block_hash=block.block_hash,
                                            prev_hash=block.prev_hash, timestamp=block.timestamp, tx=block.tx))

    def update_contract(self, contract_address: str, contract_data):
        db_service.update_contract_data(contract_address, contract_data)

    def init_genesis_block(self):
        tx = NormalTxDto(metadata='genesis')
        block = GenesisBlock(tx)
        db_service.add_data(BlockDto(block_hash=block.block_hash,
                                     prev_hash=block.prev_hash, timestamp=block.timestamp, tx=block.tx))
