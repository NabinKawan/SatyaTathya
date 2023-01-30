from app.common.service import CommonService
from app.components.block.block import Block
from datetime import datetime


class GenesisBlock(Block):

    def __init__(self, tx: str):
        self.timestamp = datetime.now().timestamp()
        self.tx = tx
        self.prev_hash = ''
        self.block_hash = CommonService.hash_block(timestamp=self.timestamp, tx=self.tx, prev_hash=self.prev_hash)
