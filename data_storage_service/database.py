import os

from pymongo import MongoClient
from pymongo import ReturnDocument

client = MongoClient("mongodb://mongo:27017/")  # Посмотреть, где будет.
db_name = os.getenv("MONGO_INITDB_DATABASE", "default_database")
db = client[db_name]


def record_data(hashed_identifier: str, data: dict, api_url: str):
    collection = db[api_url]
    # Решить с историей изменений.
    existing_record = collection.find_one_and_update(
        {"_id": hashed_identifier},
        {"$set": data},
        return_document=ReturnDocument.BEFORE,  # Можно решить с историей изменений с помощью этого (?)
        upsert=True  # Создаст новый документ, если не найдет.
    )
    pass
