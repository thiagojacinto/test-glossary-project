from os import getenv

from pydantic import BaseSettings


class Configuration(BaseSettings):
    """
    Configuration & settings wrapper using Pydantic's BaseSettings
    """

    APP_NAME: str = "TestGlossary API"
    DATABASE_CONNECTION_STRING: str = "PROVIDE A VALID DB CONNECTION STRING"

    class Config:
        """
        Sub class for handling .env file reading
        """

        env_file = ".staging.env"
        env_file_encoding = "utf-8"


if getenv("PRODUCTION_READY") == "true":
    configuration = Configuration(_env_file=".env")
else:
    configuration = Configuration()
