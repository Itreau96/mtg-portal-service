from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """db configuration loaded from environment variables."""
    db_url: str
    card_table: str

    class Config:
        env_file = ".env"

settings = Settings()