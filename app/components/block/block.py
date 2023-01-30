from abc import ABC, abstractmethod


class Block(ABC):

    @abstractmethod
    def __init__(self, tx: str):
        """
        Initialize the block
        """
        raise NotImplementedError
