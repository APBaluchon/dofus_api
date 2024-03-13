import os
from pymongo import MongoClient


class Connect:
    def __init__(self):
        self.MONGODB_HOST = os.environ.get("MONGODB_HOST", "localhost")
        self.MONGODB_PORT = int(os.environ.get("MONGODB_PORT", "27017"))
        self.MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
        self.MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")
        self.MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")

        self.client = MongoClient(
            host=self.MONGODB_HOST,
            port=self.MONGODB_PORT,
            username=self.MONGODB_USERNAME,
            password=self.MONGODB_PASSWORD,
        )
        self.db = self.client[self.MONGODB_DATABASE]

    def close(self):
        self.client.close()
