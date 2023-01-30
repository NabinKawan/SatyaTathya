import redis

redis_db = redis.Redis(
    host='127.0.0.1',
    port=6379)

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

