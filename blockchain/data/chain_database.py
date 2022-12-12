from blockchain.dto.block_dto import BlockDto
from typing import List

from blockchain.enums.data_format_enum import DataFormatEnum


class ChainDatabase(object):

    chain_datas: List[BlockDto] = []

    def __new__(cls, *args, **kwargs) -> None:
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChainDatabase, cls).__new__(
                cls, *args, **kwargs)
        return cls.instance
