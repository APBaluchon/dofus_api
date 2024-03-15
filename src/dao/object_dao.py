from dao.DB import DB


class ObjectDao:
    def __init__(self, category: str):
        """
        Initialise un objet ObjectDao avec une catégorie spécifique.

        Args:
            category (str): La catégorie des objets à récupérer.

        Returns:
            None
        """
        self.DB = DB()
        self.collection = self.DB.get_collection(category)

    def get_all_objects(self, limit: int = 10000, **filters) -> list:
        """
        Récupère tous les objets de la base de données selon les filtres spécifiés.

        Args:
            limit (int, optionnel): Limite le nombre d'objets à récupérer (par défaut 10000).
            **filters: Des filtres optionnels pour restreindre les objets récupérés.

        Returns:
            list: Une liste d'objets correspondant aux critères spécifiés.
        """

        if filters:
            query = {}
            for key, value in filters.items():
                if key == "effects":
                    query["effects." + value[0]] = {"$exists": True}
                elif key == "effects_monture":
                    query["effects.level 1." + value] = {"$exists": True}
                elif key == "drops":
                    query["drops." + value[0]] = {"$exists": True}
                elif key == "recolte":
                    query["recoltes." + value[0]] = {"$exists": True}
                elif key == "recette":
                    query["recettes." + value[0]] = {"$exists": True}
                elif key == "crafts":
                    query["crafts." + value[0]] = {"$exists": True}
                else:
                    query[key] = {"$eq": value}

            objects = list(self.collection.find(query).limit(limit))
        else:
            objects = list(self.collection.find().limit(limit))

        return objects

    def get_object_by_id(self, id: int, **filters):
        """
        Récupère un objet spécifique de la base de données par son identifiant.

        Args:
            id (int): L'identifiant unique de l'objet à récupérer.
            **filters: Des filtres optionnels pour affiner la recherche.

        Returns:
            list: Une liste d'objets correspondant à l'identifiant spécifié et aux filtres donnés.
        """

        if filters:
            query = {"_id": {"$eq": id}}
            for key, value in filters.items():
                query[key] = {"$eq": value}

            objects = list(self.collection.find(query))
        else:
            objects = list(self.collection.find({"_id": f"{id}"}))

        return objects
