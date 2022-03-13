from pymongo import MongoClient

from core.settings import settings

DB_HOST = settings.db_host
DB_PORT = settings.db_port
DB_USER = settings.db_user
DB_PASS = settings.db_password

client = MongoClient(f'mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}')
database = client.example_db
