import redis
from app.settings import configs

db_settings = configs.db_settings
redis_db = redis.Redis(
    host=db_settings.redis_host,
    port=db_settings.redis_port)

# class ChainDatabase(object):
#     """
#     Singleton Class
#     """
#     chain_datas: List[BlockDto] = []

#     def __new__(cls, *args, **kwargs) -> None:
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(ChainDatabase, cls).__new__(
#                 cls, *args, **kwargs)
#         return cls.instance
