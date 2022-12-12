import hashlib
import datetime as dt
from blockchain.services.impl.db_service import DbService


class Block:

    def __init__(self, tx, is_genesis: bool = False):
        self.timestamp = dt.datetime.now().__str__()
        self.tx = tx
        self.prev_hash = DbService.get_prev_hash(is_genesis=is_genesis)
        self.block_hash = self.hash_block()

    def hash_block(self):
        all_data = str(self.timestamp)+str(self.tx)+str(self.prev_hash)
        return hashlib.sha256(all_data.encode()).hexdigest()
