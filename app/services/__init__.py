from app.models.enums.db_enum import DbTypeEnum
from app.services.db_service import DbService
from app.services.impl.local_db_service import LocalDbService
from app.settings import configs
from typing import Type

db_service: DbService = LocalDbService()


def get_db_service() -> Type[DbService]:
    if configs.db_settings.type == DbTypeEnum.LOCAL:
        return LocalDbService
