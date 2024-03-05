from DAO.connect import Connect

class RessourcesDao:
    def __init__(self):
        self.connect = Connect("dofusdb", "ressources")
        self.collection = self.connect.get_collection()

    def get_all_ressources(self, limit: int = 10000) -> list:
        ressources = list(self.collection.find())

        return ressources
    
    def get_ressource_by_id(self, id: int):
        ressource = self.collection.find({ "_id": f'{id}' })

        return list(ressource)
