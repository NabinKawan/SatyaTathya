import json

from app.models.enums.data_format_enum import DataFormatEnum
from app.services.impl.khwopa_service import KhwopaService
from app.services import db_service
from app.settings import configs
from server import run_server

blockchain_settings = configs.blockchain_settings


def init_genesis_block():
    khwopa_service = KhwopaService()
    blocks = db_service.get_all_datas()
    if (len(blocks) == 0):
        khwopa_service.init_genesis_block()


def main() -> None:
    # init_genesis_block()
    run_server()


if __name__ == '__main__':
    main()
