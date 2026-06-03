from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

try:
    client = MongoClient(os.getenv("MONGO_DB"))
    db = client["shopee_integration"]
    products = db["products"]
except Exception as ex:
    print(ex)
