from pydantic import BaseModel, Json
from typing import Union, Any


class ContractTxDto(BaseModel):
    byte_code: str
    contract_data: str


class NormalTxDto(BaseModel):
    metadata: str


class BlockDto(BaseModel):
    block_hash: str
    prev_hash: str
    timestamp: float
    tx: Union[ContractTxDto, NormalTxDto]
