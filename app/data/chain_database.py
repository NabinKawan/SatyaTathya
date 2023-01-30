from app.models.dtos.block_dto import BlockDto
from typing import List


class ChainDatabase(object):
    """
    Singleton Class
    """
    chain_datas: List[BlockDto] = []

    def __new__(cls, *args, **kwargs) -> None:
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChainDatabase, cls).__new__(
                cls, *args, **kwargs)
        return cls.instance
