from Object.EntityObject import EntityObject
from Scraper.MonstreScraper import MonstreScraper
from Utils.utils import converts_effects_to_dict

class MonstreObject(EntityObject):
    def __init__(self, url: str):
        self.drops = dict()
        super().__init__(url)
        
    def use_scraper(self):
        scraper = MonstreScraper(self.url)
        self.name = scraper.get_name()
        self.id = scraper.get_id()
        self.race = scraper.get_type()
        self.level = scraper.get_level()
        self.image = scraper.get_image()
        self.drops = scraper.get_drops()
        self.zone = scraper.get_zone()
        self.characteristcs = scraper.get_characteristics()
        self.resistances = scraper.get_resistances()

    # def to_json(self) -> dict:
    #     json = super().to_json()
    #     json['effects'] = converts_effects_to_dict(self.effects)
    #     json['conditions'] = self.conditions
    #     return json
