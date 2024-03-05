from Object.RessourceObject import RessourceObject
from DAO.connect import Connect

class RessourcesDao:
    def __init__(self):
        self.connect = Connect("dofusdb", "ressources")
        self.collection = self.connect.get_collection()

    def read_all_ressources(self, limit: int = 10000) -> list[RessourceObject]:
        ressources = list(self.collection.find())

        return ressources
