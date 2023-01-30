from app.common.service import CommonService
from app.components.block.block import Block
from datetime import datetime

from app.services.impl.local_db_service import LocalDbService

db_service = LocalDbService()


class NormalBlock(Block):

    def __init__(self, tx):
        self.timestamp = datetime.now().timestamp()
        self.tx = tx
        self.prev_hash = ''
        self.block_hash = CommonService.hash_block(timestamp=self.timestamp, tx=self.tx, prev_hash=self.prev_hash)
