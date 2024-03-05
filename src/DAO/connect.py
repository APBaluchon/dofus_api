import pymongo

class Connect:
    def __init__(self, db, collection, password):
        self.client = pymongo.MongoClient(f"mongodb+srv://admin:{password}@dofusdb.5yaaqce.mongodb.net/?retryWrites=true&w=majority&appName=dofusdb")
        self.db = self.client[db]
        self.collection = self.db[collection]
    def get_collection(self):
        return self.collection
    def close(self):
        self.client.close()
