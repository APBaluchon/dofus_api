import pymongo
import os
import dotenv

class Connect:
    def __init__(self, db: str):
        dotenv.load_dotenv(override=True)
        username = os.environ["username"]
        password = os.environ["password"]

        self.client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@dofusdb.5yaaqce.mongodb.net/?retryWrites=true&w=majority&appName=dofusdb")
        self.db = self.client[db]
    def close(self):
        self.client.close()
