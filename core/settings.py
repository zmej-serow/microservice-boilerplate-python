from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    db_user: str = os.environ.get('DB_USER', 'admin')
    db_password: str = os.environ.get('DB_PASS', 'admin_pass')
    db_name: str = os.environ.get('DB_NAME', 'example_db')
    db_host: str = os.environ.get('DB_HOST', 'service_mongodb')
    db_port: int = os.environ.get('DB_PORT', 27017)

    class Config:
        env_file = "core/.env"


settings = Settings()
