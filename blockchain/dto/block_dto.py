from pydantic import BaseModel


class BlockDto(BaseModel):
    block_hash: str
    prev_hash: str
    timestamp: str
    tx: str
