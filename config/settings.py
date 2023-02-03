import os
from pydantic import BaseSettings, SecretStr
import pathlib
from dotenv import load_dotenv

config_path = pathlib.Path(__file__).resolve().parent


class GlobalSettings(BaseSettings):
    ENV_STATE: str = os.environ.get("CRAWLING_MODE", "dev")
    APP_ENV: str = ENV_STATE
    CONFIG_PATH: str = str(config_path)
    PROJECT_PATH: str = str(config_path.parent)

    class Config:
        env_file = f"{config_path}/envs/.env"


class DevSettings(GlobalSettings):
    IPO_URL: str
    LISTING_SERVER_IP: str
    WEB_SERVER_IP: str
    DB_HOST: str
    DB_IPOLISTING: str
    DB_GOOGLENEWS: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: str
    SLACK_WEB_HOOK_URL: str
    REALTIME_PRICE_PAST_API: str
    REALTIME_PRICE_API: str
    DB_NAME: str
    DELISTING: str = "공모철회"

    class Config:
        env_file = f"{config_path}/envs/dev.env"


class ProdSettings(GlobalSettings):
    IPO_URL: str
    LISTING_SERVER_IP: str
    WEB_SERVER_IP: str
    DB_HOST: str
    DB_IPOLISTING: str
    DB_GOOGLENEWS: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: str
    SLACK_WEB_HOOK_URL: str
    REALTIME_PRICE_PAST_API: str
    REALTIME_PRICE_API: str
    DB_NAME: str
    DELISTING: str = "공모철회"

    class Config:
        env_file = f"{config_path}/envs/prod.env"


class TestSettings(GlobalSettings):
    IPO_URL: str
    LISTING_SERVER_IP: str
    WEB_SERVER_IP: str
    DB_HOST: str
    DB_IPOLISTING: str
    DB_GOOGLENEWS: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: str
    SLACK_WEB_HOOK_URL: str
    REALTIME_PRICE_PAST_API: str
    REALTIME_PRICE_API: str
    DB_NAME: str
    DELISTING: str = "공모철회"

    class Config:
        env_file = f"{config_path}/envs/test.env"


class FactorySettings:
    @staticmethod
    def load():
        ENV_STATE = GlobalSettings().ENV_STATE
        if ENV_STATE == "dev":
            return DevSettings()
        elif ENV_STATE == "prod":
            return ProdSettings()
        elif ENV_STATE == "test":
            return TestSettings()


settings = FactorySettings.load()

IPO_URL = settings.IPO_URL
CONFIG_PATH = settings.CONFIG_PATH
PROJECT_PATH = settings.PROJECT_PATH
LISTING_SERVER_IP = settings.LISTING_SERVER_IP
WEB_SERVER_IP = settings.WEB_SERVER_IP

DB_HOST = settings.DB_HOST
DB_IPOLISTING = settings.DB_IPOLISTING
DB_GOOGLENEWS = settings.DB_GOOGLENEWS
DB_USER = settings.DB_USER
DB_PASSWORD = settings.DB_PASSWORD
DB_PORT = settings.DB_PORT
DB_NAME = settings.DB_NAME

SLACK_WEB_HOOK_URL = settings.SLACK_WEB_HOOK_URL

REALTIME_PRICE_PAST_API = settings.REALTIME_PRICE_PAST_API
REALTIME_PRICE_API = settings.REALTIME_PRICE_API
REALTIME_PRICE_API = settings.REALTIME_PRICE_API
DELISTING = settings.DELISTING

if __name__ == "__main__":

    has_attr = hasattr(settings, "SLACK_WEB_HOOK_URL")
    print(has_attr)
    print(settings.LISTING_SERVER_IP)
    print(settings.WEB_SERVER_IP)
    print(settings.DB_HOST)
    # print(settings.DB_IPOLISTING)
    # print(settings.DB_GOOGLENEWS)
    # print(settings.DB_USER)
    # print(settings.DB_PASSWORD)
    # print(settings.DB_PORT)
    # print(settings.DB_NAME)
    # print(settings.SLACK_WEB_HOOK_URL)
    # print(settings.REALTIME_PRICE_PAST_API)
    # print(settings.REALTIME_PRICE_API)
    # print(settings.REALTIME_PRICE_API)
    # print(settings.PROJECT_PATH)
