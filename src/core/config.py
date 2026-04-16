from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PDF Extract"
    app_version: str = "1.0.0"
    debug: bool = False

    database_url: str = "sqlite:///./data/app.db"

    max_file_size_mb: int = 50

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
