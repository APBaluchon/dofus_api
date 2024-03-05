from DAO.connect import Connect

class ObjectDao:
    def __init__(self, category: str):
        self.connect = Connect("dofusdb", category)
        self.collection = self.connect.get_collection()

    def get_all_objects(self, limit: int = 10000) -> list:
        objects = list(self.collection.find())

        return objects
    
    def get_object_by_id(self, id: int):
        object = self.collection.find({ "_id": f'{id}' })

        return list(object)
