from DAO.connect import Connect
from Object.EntityObject import EntityObject

class FillDB:
    def __init__(self, db, collection, password):
        self.connect = Connect(db, collection, password)
        self.collection = self.connect.get_collection()
    def insert(self, data: EntityObject):
        self.collection.insert_one(data.to_json())
    def insert_many(self, data: list[EntityObject]):
        self.collection.insert_many([item.to_json() for item in data])
    def exists(self, data: EntityObject):
        return self.collection.find_one(data.to_json()) != None
    def close(self):
        self.connect.close()

