from blockchain.enums.data_format_enum import DataFormatEnum
from blockchain.services.impl.db_service import DbService
from blockchain.services.impl.khwopa_blockchain import KhwopaBlockchain


if __name__ == '__main__':
    blk = KhwopaBlockchain()
    blk.init_genesis_block()
    blk.add_block('ram to shyam :3 btc')
    blk.add_block("sita to gita: 2 btc")
    blk.add_block("hari to harry: 2 btc")

    datas = DbService.get_all_datas()
    print(datas)
