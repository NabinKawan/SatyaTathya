from abc import ABC, abstractmethod


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
    def init_genesis_block(self):
        """
        Initialize genesis block
        """
        raise NotImplementedError
