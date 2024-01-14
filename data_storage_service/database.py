import os

from pymongo import MongoClient
from pymongo import ReturnDocument


host = "mongo"
port = 27017
username = os.getenv("MONGO_INITDB_ROOT_USERNAME", "username")
password = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "password")

client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
db_name = os.getenv("MONGO_INITDB_DATABASE", "default_database")
db = client[db_name]


def record_data(hashed_identifier: str, data: dict, api_url: str):
    collection = db[api_url]
    existing_record = collection.find_one_and_update(
        {"_id": hashed_identifier},
        {"$set": data},
        return_document=ReturnDocument.BEFORE,
        upsert=True,
    )
    if existing_record:
        history_collection = db["history_" + api_url]
        history_collection.insert_one(existing_record)


def get_data(url: str):  # TODO: Удалить это
    collection = db[url]
    documents = collection.find()
    return [doc for doc in documents]
