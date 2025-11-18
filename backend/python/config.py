import os
from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FileOrganizer Pro"
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    db_path: Path = Path.home() / ".fileorganizer" / "database.db"

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()

# BUGFIX: Add parents=True to create intermediate directories
settings.db_path.parent.mkdir(parents=True, exist_ok=True)
