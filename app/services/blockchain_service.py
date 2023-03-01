from abc import ABC, abstractmethod
from pydantic import Json
from typing import Any


class BlockchainService(ABC):
    """
    Abstract base class for blockchain services.
    """

    @abstractmethod
    def add_block(self, tx: str):
        """
        Add block
        """
        raise NotImplementedError

    @abstractmethod
    def add_contract(self, byte_code: str, contract_data: str):
        """
                Add contract
                """
        raise NotImplementedError

    @abstractmethod
    def init_genesis_block(self):
        """
        Initialize genesis block
        """
        raise NotImplementedError
