import hashlib
import datetime


class CommonService:

    @staticmethod
    def hash_block(timestamp: str, tx: str, prev_hash: str):
        """
        Hash the content of the block

        Args:
            timestamp (str): timestamp of the block
            tx (str): tx
            prev_hash (str): hash of previous block

        Returns:
            HexDigest
        """

        to_hash = f"{timestamp}{tx}{prev_hash}"
        return hashlib.sha256(to_hash.encode()).hexdigest()
