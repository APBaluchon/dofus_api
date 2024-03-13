from object.entity_object import EntityObject
from scraper.monstre_scraper import MonstreScraper


class MonstreObject(EntityObject):
    def __init__(self, url: str):
        self.drops = dict()
        self.scraper = None
        super().__init__(url)

    def use_scraper(self):
        self.scraper = MonstreScraper(self.url)
        self.name = self.scraper.get_name()
        self.id = self.scraper.get_id()
        self.race = self.scraper.get_type()
        self.level = self.scraper.get_level()
        self.image = self.scraper.get_image()
        self.drops = self.scraper.get_drops()
        self.characteristics = self.scraper.get_characteristics()

    def to_json(self) -> dict:
        dic = {
            "id": self.id,
            "name": self.name,
            "race": self.race,
            "drops": self.drops,
            "caracteristics": self.characteristics,
            "resistances": self.scraper.get_resistances(),
        }
        if self.scraper.has_zone():
            dic["zone"] = self.scraper.get_zone()
        return dic
