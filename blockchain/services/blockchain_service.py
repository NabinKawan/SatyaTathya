from abc import ABC, abstractmethod


class BlockchainService(ABC):

    @abstractmethod
    def add_block(self, tx: str):
        pass

    @abstractmethod
    def init_genesis_block(self):
        pass
