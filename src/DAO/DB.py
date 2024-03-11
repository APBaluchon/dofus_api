from typing import List, Optional
import logging
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import PyMongoError
from Object.EntityObject import EntityObject
from Object.ConsommableObject import ConsommableObject
from Object.RessourceObject import RessourceObject
from Object.MontureObject import MontureObject
from DAO.Connect import Connect
from Utils.utils import get_all_links
from time import sleep
from Scraper.EntityScraper import EntityScraper

class DB:
    def __init__(self, db_name: str):
        self.db = Connect(db_name).db

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
    
    def entity_is_not_empty(self, collection_name: str, entity_id: str) -> bool:
        collection = self.get_collection(collection_name)
        if collection is not None:
            if self.entity_exists(collection_name, entity_id): 
                return collection.find_one({"_id": entity_id})["name"] is not None
        return False


    def insert_with_url(self, collection_name: str, url: str) -> int:
        scraper = EntityScraper(url)
        entity_id = scraper.get_id()

        if self.entity_exists(collection_name, entity_id) & self.entity_is_not_empty(collection_name, entity_id):
            return 0
        else:
            if collection_name == "consommables":
                entity = ConsommableObject(url)
            elif collection_name == "ressources":
                entity = RessourceObject(url)
            elif collection_name == "montures":
                entity = MontureObject(url)
            else:
                logging.error("Invalid collection name")
                return 0
            if not self.entity_exists(collection_name, entity_id):
                self.insert_entity(collection_name, entity)
            else:
                self.replace_entity(collection_name, entity_id, entity)
            return 1

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
        num_inserted = 0
        for url in links:
            num_inserted += self.insert_with_url(cat, url)
            if cat == "montures":
                sleep(180)
            else:
                if num_inserted % 100 == 0:
                    logging.info(f"{num_inserted} entities inserted")
                    sleep(180)
