from DAO.DB import DB

class ObjectDao:
    def __init__(self, category: str):
        self.DB = DB("dofusdb")
        self.collection = self.DB.get_collection(category)

    def get_all_objects(self, limit: int = 10000) -> list:
        objects = list(self.collection.find())
        print(objects)

        return objects
    
    def get_object_by_id(self, id: int):
        object = self.collection.find({ "_id": f'{id}' })

        return list(object)
