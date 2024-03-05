import pymongo
import os
import dotenv

class Connect:
    def __init__(self, db, collection):
        dotenv.load_dotenv(override=True)
        username = os.environ["username"]
        password = os.environ["password"]

        self.client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@dofusdb.5yaaqce.mongodb.net/?retryWrites=true&w=majority&appName=dofusdb")
        self.db = self.client[db]
        self.collection = self.db[collection]
    def get_collection(self):
        return self.collection
    def close(self):
        self.client.close()
