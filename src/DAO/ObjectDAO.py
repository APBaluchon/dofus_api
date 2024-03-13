from DAO.DB import DB

class ObjectDao:
    def __init__(self, category: str):
        self.DB = DB("dofusdb")
        self.collection = self.DB.get_collection(category)

    def get_all_objects(self, limit: int = 10000, **filters) -> list:

        if filters:
            query = {}
            for key, value in filters.items():
                if key == "effects":
                    query["effects." + value[0]] = {"$exists": True}
                elif key == "drops":
                    query["drops." + value[0]] = {"$exists": True}
                elif key == "effects_monture":
                    query["effects.level 1." + value] = {"$exists": True}
                else:
                    query[key] = { "$eq": value }

            objects = list(self.collection.find(query).limit(limit))
        else:
            objects = list(self.collection.find().limit(limit))

        return objects
    
    def get_object_by_id(self, id: int,  **filters):

        if filters:
            query = {"_id": { "$eq": id }}
            for key, value in filters.items():
                query[key] = { "$eq": value }

            objects = list(self.collection.find(query))
        else:
            objects = list(self.collection.find({ "_id": f'{id}' }))

        return objects
