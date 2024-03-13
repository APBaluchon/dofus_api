from object.entity_object import EntityObject
from scraper.metier_scraper import MetierScraper
from utils.utils import converts_effects_to_dict


class MetierObject(EntityObject):
    def __init__(self, url: str):
        self.drops = dict()
        self.scraper = None
        super().__init__(url)

    def use_scraper(self):
        self.scraper = MetierScraper(self.url)
        self.name = self.scraper.get_name()
        self.id = self.scraper.get_id()
        self.image = self.scraper.get_image()
        self.desc = self.scraper.get_description()

    def to_json(self) -> dict:
        dic = {
            "_id": self.id,
            "name": self.name,
            "image": self.image,
            "description": self.desc,
        }
        if self.scraper.has_recettes():
            dic["recettes"] = self.scraper.get_recettes()
        if self.scraper.has_recoltes():
            dic["recoltes"] = self.scraper.get_recoltes()
        return dic
