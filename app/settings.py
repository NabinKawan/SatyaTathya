from pydantic import BaseSettings


class DbSettings(BaseSettings):
    type: str = 'local'

    class Config:
        env_prefix = 'DB_'


class Settings(BaseSettings):
    db_settings = DbSettings()


def get_configs():
    return Settings()


configs = get_configs()
