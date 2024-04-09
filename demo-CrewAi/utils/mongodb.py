from pymongo import MongoClient
import os

client = None
db = None

def open_connection():
    global client, db
    client = MongoClient(os.getenv("MONGO_CLIENT_URI"))
    db = client.Managment
    return db

def close_connection():
    global client
    if client is not None:
        client.close()
        client = None

