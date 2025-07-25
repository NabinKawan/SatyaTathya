import pydantic


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class DbSettings(BaseSettings):
    host: str = "local"
    port: int = 6379

    class Config:
        env_prefix = "DB_"


class BlockChainSettings(BaseSettings):
    port: int = 5005
    host: str = "localhost"
    name: str = "SatyaTathya"

    class Config:
        env_prefix = "BLOCKCHAIN_"


class Settings(BaseSettings):
    db_settings = DbSettings()
    blockchain_settings = BlockChainSettings()


def get_configs():
    return Settings()


configs = get_configs()
