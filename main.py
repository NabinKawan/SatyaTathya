from app.models.enums.data_format_enum import DataFormatEnum
from app.services.impl.khwopa_service import KhwopaService
from app.services import db_service


def main() -> None:
    khwopa_service = KhwopaService()
    khwopa_service.init_genesis_block()
    khwopa_service.add_block('ram to shyam :3 btc')

    # default_datas = db_service.get_all_datas()
    # print(default_datas)
    # json_datas = db_service.get_all_datas(data_type=DataFormatEnum.JSON)
    # print(json_datas )
    # print("\n")

if __name__ == '__main__':
    main()







