from blockchain.block import Block
from blockchain.dto.block_dto import BlockDto
from blockchain.services.impl.db_service import DbService
from blockchain.services.blockchain_service import BlockchainService


class KhwopaBlockchain(BlockchainService):

    def add_block(self, tx: str):
        block = Block(tx)
        DbService.add_data(BlockDto(block_hash=block.block_hash,
                           prev_hash=block.prev_hash, timestamp=block.timestamp, tx=block.tx))

    def init_genesis_block(self):
        block = Block('genesis', is_genesis=True)
        DbService.add_data(BlockDto(block_hash=block.block_hash,
                           prev_hash=block.prev_hash, timestamp=block.timestamp, tx=block.tx))
