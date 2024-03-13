from dao.config import MONGODB_HOST, MONGODB_PORT, MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_DATABASE
from pymongo import MongoClient


class Connect:
    def __init__(self):
        self.MONGODB_HOST = MONGODB_HOST
        self.MONGODB_PORT = MONGODB_PORT
        self.MONGODB_USERNAME = MONGODB_USERNAME
        self.MONGODB_PASSWORD = MONGODB_PASSWORD
        self.MONGODB_DATABASE = MONGODB_DATABASE

        self.client = MongoClient(
            host=self.MONGODB_HOST,
            port=self.MONGODB_PORT,
            username=self.MONGODB_USERNAME,
            password=self.MONGODB_PASSWORD,
        )
        self.db = self.client[self.MONGODB_DATABASE]

    def close(self):
        self.client.close()
