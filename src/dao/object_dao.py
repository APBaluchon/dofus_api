import logging
from typing import Optional

from dao.DB import DB
from pymongo.errors import PyMongoError


class ObjectDao:
    """Data access helper for Mongo collections."""

    DEFAULT_LIMIT = 10000

    def __init__(self, category: str):
        """
        Initialise un objet ObjectDao avec une catégorie spécifique.

        Args:
            category (str): La catégorie des objets à récupérer.
        """

        self.DB = DB()
        self.collection = self.DB.get_collection(category)

    @staticmethod
    def _sanitize_limit(limit: int) -> int:
        """Retourne un plafond de résultats sûr pour MongoDB."""

        try:
            numeric_limit = int(limit)
        except (TypeError, ValueError):
            return ObjectDao.DEFAULT_LIMIT

        if numeric_limit <= 0:
            return ObjectDao.DEFAULT_LIMIT

        return min(numeric_limit, ObjectDao.DEFAULT_LIMIT)

    def get_all_objects(self, limit: int = DEFAULT_LIMIT, **filters) -> list:
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

        limit_value = self._sanitize_limit(limit)

        if not filters:
            try:
                return list(collection.find().limit(limit_value))
            except PyMongoError as err:
                logging.error("Error while listing %s: %s", self.collection.name, err)
                return []

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

        try:
            return list(collection.find(query).limit(limit_value))
        except PyMongoError as err:
            logging.error(
                "Error while querying %s with filters %s: %s",
                self.collection.name,
                filters,
                err,
            )
            return []

    def get_object_by_id(self, id: str, **filters) -> Optional[dict]:
        """
        Récupère un objet spécifique de la base de données par son identifiant.

        Args:
            id (int): L'identifiant unique de l'objet à récupérer.
            **filters: Des filtres optionnels pour affiner la recherche.

        Returns:
            dict | None: L'objet correspondant ou None s'il est absent.
        """

        collection = self.collection
        if collection is None:
            return None

        str_id = str(id)
        query = {"_id": str_id}
        for key, value in filters.items():
            query[key] = {"$eq": value}

        try:
            document = collection.find_one(query)
        except PyMongoError as err:
            logging.error("Error while fetching %s/%s: %s", self.collection.name, str_id, err)
            return None

        if document is None and str_id.isdigit():
            numeric_id = int(str_id)
            query["_id"] = numeric_id
            try:
                document = collection.find_one(query)
            except PyMongoError as err:
                logging.error(
                    "Error while fetching %s/%s as numeric: %s",
                    self.collection.name,
                    numeric_id,
                    err,
                )
                return None

        return document
