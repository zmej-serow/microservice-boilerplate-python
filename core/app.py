from datetime import datetime
from fastapi import FastAPI

from core.db import database

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.post('/in/{kek}')
async def insert_kek(kek: str):
    kek_data = {
        'kek': kek,
        'date': datetime.utcnow(),
    }
    collection = database.get_collection('example_colly')
    document_id = collection.insert_one(kek_data).inserted_id
    return {'id': str(document_id)}


@app.get('/out/{kek}')
async def fetch_kek(kek: str):
    kek_query = {
        'kek': kek,
    }
    collection = database.get_collection('example_colly')
    kek_document = collection.find_one(kek_query)
    return {'result': str(kek_document)}
