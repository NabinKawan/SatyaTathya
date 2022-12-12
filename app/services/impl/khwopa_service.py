from app.components.block.impl.genesis_block import GenesisBlock
from app.components.block.impl.normal_block import NormalBlock
from app.models.dtos.block_dto import BlockDto
from app.services.blockchain_service import BlockchainService
from app.services import db_service


class KhwopaService(BlockchainService):

    def add_block(self, tx: str):
        block = NormalBlock(tx)
        db_service.add_data(BlockDto(block_hash=block.block_hash,
                                     prev_hash=block.prev_hash, timestamp=block.timestamp, tx=block.tx))

    def init_genesis_block(self):
        block = GenesisBlock('genesis')
        db_service.add_data(BlockDto(block_hash=block.block_hash,
                                     prev_hash=block.prev_hash, timestamp=block.timestamp, tx=block.tx))
