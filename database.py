from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

try:
    client = MongoClient(os.getenv("MONGO_DB"))
    db = client["FirstDatabase"]
    users = db["users"]
except Exception as ex:
    print(ex)
