from typing import List, Optional
import logging
import time
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import PyMongoError
from object.entity_object import EntityObject
from object.consommable_object import ConsommableObject
from object.ressource_object import RessourceObject
from object.monture_object import MontureObject
from object.monstre_object import MonstreObject
from object.metier_object import MetierObject
from object.equipement_object import EquipementObject
from dao.connect import Connect
from utils import utils


class DB:
    """
    Classe pour interagir avec une base de données MongoDB.

    Attributes:
        db (Database): Connexion à la base de données.

    Methods:
        __init__() -> None:
            Initialise une instance de la classe DB.

        get_collection(collection_name: str) -> Optional[Collection]:
            Récupère une collection de la base de données.

        insert_entity(collection_name: str, data: EntityObject) -> None:
            Insère une entité dans la collection spécifiée.

        replace_entity(collection_name: str, entity_id: str, data: EntityObject) -> None:
            Remplace une entité existante dans la collection spécifiée.

        entity_exists(collection_name: str, entity_id: str) -> bool:
            Vérifie si une entité avec l'ID spécifié existe dans la collection spécifiée.

        insert_with_url(collection_name: str, url: str) -> None:
            Insère une entité dans la collection spécifiée en utilisant une URL.

        insert_many_entities(collection_name: str, data: List[EntityObject]) -> None:
            Insère plusieurs entités dans la collection spécifiée.

        fill(cat: str) -> None:
            Remplit la base de données avec les entités provenant des liens de la catégorie spécifiée.
    """
    def __init__(self):
        """
        Initialise une instance de la classe DB avec le nom de la base de données.
        """
        self.db = Connect().db

    def get_collection(self, collection_name: str) -> Optional[Collection]:
        """
        Récupère une collection de la base de données.

        Args:
            collection_name (str): Le nom de la collection à récupérer.

        Returns:
            Optional[Collection]: La collection récupérée, ou None si une erreur survient.
        """
        try:
            return self.db[collection_name]
        except PyMongoError as e:
            logging.error(f"Error getting collection: {e}")
            return None

    def insert_entity(self, collection_name: str, data: EntityObject):
        """
        Insère une entité dans la collection spécifiée.

        Args:
            collection_name (str): Le nom de la collection dans laquelle insérer l'entité.
            data (EntityObject): L'objet représentant l'entité à insérer.
        """
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                collection.insert_one(data.to_json())
            except PyMongoError as e:
                logging.error(f"Error inserting entity: {e}")
        else:
            logging.error("Invalid collection name")

    def replace_entity(self, collection_name: str, entity_id: str, data: EntityObject):
        """
        Remplace une entité existante dans la collection spécifiée.

        Args:
            collection_name (str): Le nom de la collection dans laquelle remplacer l'entité.
            entity_id (str): L'identifiant de l'entité à remplacer.
            data (EntityObject): L'objet représentant la nouvelle entité.
        """
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                collection.replace_one({"_id": entity_id}, data.to_json())
            except PyMongoError as e:
                logging.error(f"Error replacing entity: {e}")
        else:
            logging.error("Invalid collection name")

    def entity_exists(self, collection_name: str, entity_id: str) -> bool:
        """
        Vérifie si une entité avec l'identifiant donné existe dans la collection spécifiée.

        Args:
            collection_name (str): Le nom de la collection à vérifier.
            entity_id (str): L'identifiant de l'entité à rechercher.

        Returns:
            bool: True si l'entité existe, False sinon.
        """
        collection = self.get_collection(collection_name)
        if collection is not None:
            return collection.find_one({"_id": entity_id}) is not None
        return False

    def insert_with_url(self, collection_name: str, url: str):
        """
        Insère une entité dans la collection spécifiée en fonction de l'URL fournie.

        Args:
            collection_name (str): Le nom de la collection dans laquelle insérer l'entité.
            url (str): L'URL à partir de laquelle créer l'entité.
        """
        if collection_name == "consommables":
            entity = ConsommableObject(url)
        elif collection_name == "ressources":
            entity = RessourceObject(url)
        elif collection_name == "montures":
            entity = MontureObject(url)
        elif collection_name == "monstres":
            entity = MonstreObject(url)
        elif collection_name == "metiers":
            entity = MetierObject(url)
        elif collection_name == "equipements":
            if utils.get_content_page(url) == "404":
                return None
            entity = EquipementObject(url)
            if entity.name is None:
                raise(AttributeError("Erreur 403"))
        else:
            logging.error("Invalid collection name")
            return

        if self.entity_exists(collection_name, entity.id):
            self.replace_entity(collection_name, entity.id, entity)
        else:
            self.insert_entity(collection_name, entity)

    def insert_many_entities(self, collection_name: str, data: List[EntityObject]):
        """
        Insère plusieurs entités dans la collection spécifiée.

        Args:
            collection_name (str): Le nom de la collection dans laquelle insérer les entités.
            data (List[EntityObject]): La liste des objets représentant les entités à insérer.
        """
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                collection.insert_many([item.to_json() for item in data])
            except PyMongoError as e:
                logging.error(f"Error inserting many entities: {e}")

    def fill(self, cat: str):
        """
        Remplit la base de données avec des entités de la catégorie spécifiée.

        Args:
            cat (str): La catégorie à remplir.
        """
        utils.get_all_links(cat, "src/links/temp_links.txt")
        links = open("src/links/temp_links.txt", "r").read().split("\n")
        for url in links:
            while True:
                try:
                    self.insert_with_url(cat, url)
                    break
                except Exception as e:
                    print(e, "Retrying in 3 minutes")
                    time.sleep(180)
