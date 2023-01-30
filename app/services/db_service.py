from app.models.dtos.block_dto import BlockDto
from app.models.enums.data_format_enum import DataFormatEnum
from abc import ABC, abstractmethod


class DbService(ABC):
    """
    Abstract base class for database services.
    """

    @abstractmethod
    def add_data(self, block: BlockDto):
        """
        Add block to db
        """

        raise NotImplementedError

    @abstractmethod
    def get_prev_hash(self):
        """
        Get previous block hash in a chain
        """

        raise NotImplementedError

    @abstractmethod
    def get_all_datas(self, data_type: DataFormatEnum = DataFormatEnum.BLOCK):
        """
        Get all blocks from db

        Args:
            data_type: Type of data format for block
        """
        raise NotImplementedError
