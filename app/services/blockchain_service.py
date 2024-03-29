from abc import ABC, abstractmethod
from pydantic import Json
from typing import Any


class BlockchainService(ABC):
    """
    Abstract base class for blockchain services.
    """

    @abstractmethod
    def add_block(self, tx: any):
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
    def update_contract(self, contract_address: str, contract_data):
        """
        Update contract
        """
        raise NotImplementedError

    @abstractmethod
    def init_genesis_block(self):
        """
        Initialize genesis block
        """
        raise NotImplementedError
