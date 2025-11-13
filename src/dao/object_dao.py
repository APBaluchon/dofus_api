from typing import Optional

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

        collection = self.collection
        if collection is None:
            return []

        if not filters:
            return list(collection.find().limit(limit))

        query = {}
        for key, value in filters.items():
            if value is None:
                continue

            if key == "effects":
                query[f"effects.{value}"] = {"$exists": True}
            elif key == "effects_monture":
                query[f"effects.level 1.{value}"] = {"$exists": True}
            elif key in {"drops", "recolte", "recette", "crafts"}:
                field_mapping = {
                    "drops": "drops",
                    "recolte": "recoltes",
                    "recette": "recettes",
                    "crafts": "crafts",
                }
                query[f"{field_mapping[key]}.{value}"] = {"$exists": True}
            else:
                query[key] = {"$eq": value}

        return list(collection.find(query).limit(limit))

    def get_object_by_id(self, id: str, **filters) -> Optional[dict]:
        """
        Récupère un objet spécifique de la base de données par son identifiant.

        Args:
            id (int): L'identifiant unique de l'objet à récupérer.
            **filters: Des filtres optionnels pour affiner la recherche.

        Returns:
            list: Une liste d'objets correspondant à l'identifiant spécifié et aux filtres donnés.
        """

        collection = self.collection
        if collection is None:
            return None

        str_id = str(id)
        query = {"_id": str_id}
        for key, value in filters.items():
            query[key] = {"$eq": value}

        document = collection.find_one(query)
        if document is None and str_id.isdigit():
            numeric_id = int(str_id)
            query["_id"] = numeric_id
            document = collection.find_one(query)

        return document
