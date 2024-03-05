from DAO.connect import Connect
from Object.EntityObject import EntityObject

class FillDB:
    def __init__(self, db, collection):
        self.connect = Connect(db, collection)
        self.collection = self.connect.get_collection()
    def insert(self, data: EntityObject):
        self.collection.insert_one(data.to_json())
    def insert_many(self, data: list[EntityObject]):
        self.collection.insert_many([item.to_json() for item in data])
    def replace(self, data: EntityObject):
        self.collection.replace_one({"_id": data.id}, data.to_json())
    def object_exists(self, data: EntityObject):
        return self.collection.find_one(data.to_json()) != None
    def id_exists(self, id: int):
        return self.collection.find_one({"_id": id}) != None
    def close(self):
        self.connect.close()

