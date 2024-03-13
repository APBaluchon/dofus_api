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
from utils.utils import get_all_links


class DB:
    def __init__(self, db_name: str):
        self.db = Connect().db

    def get_collection(self, collection_name: str) -> Optional[Collection]:
        try:
            return self.db[collection_name]
        except PyMongoError as e:
            logging.error(f"Error getting collection: {e}")
            return None

    def insert_entity(self, collection_name: str, data: EntityObject):
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                collection.insert_one(data.to_json())
            except PyMongoError as e:
                logging.error(f"Error inserting entity: {e}")

    def replace_entity(self, collection_name: str, entity_id: str, data: EntityObject):
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                collection.replace_one({"_id": entity_id}, data.to_json())
            except PyMongoError as e:
                logging.error(f"Error replacing entity: {e}")

    def entity_exists(self, collection_name: str, entity_id: str) -> bool:
        collection = self.get_collection(collection_name)
        if collection is not None:
            return collection.find_one({"_id": entity_id}) is not None
        return False

    def insert_with_url(self, collection_name: str, url: str):
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
            entity = EquipementObject(url)
        else:
            logging.error("Invalid collection name")
            return

        if self.entity_exists(collection_name, entity.id):
            self.replace_entity(collection_name, entity.id, entity)
        else:
            self.insert_entity(collection_name, entity)

    def insert_many_entities(self, collection_name: str, data: List[EntityObject]):
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                collection.insert_many([item.to_json() for item in data])
            except PyMongoError as e:
                logging.error(f"Error inserting many entities: {e}")

    def fill(self, cat: str):
        get_all_links(cat, "src/links/temp_links.txt")
        links = open("src/links/temp_links.txt", "r").read().split("\n")
        for url in links:
            while True:
                try:
                    self.insert_with_url(cat, url)
                    break
                except Exception as e:
                    print(e, "Retrying in 3 minutes")
                    time.sleep(180)