from Object.EntityObject import EntityObject
from Scraper.ConsommableScraper import ConsommableScraper
from Utils.utils import converts_effects_to_dict

class ConsommableObject(EntityObject):
    def __init__(self, url: str):
        self.effects = []
        self.conditions = []
        super().__init__(url)
        
    def use_scraper(self):
        scraper = ConsommableScraper(self.url)
        self.name = scraper.get_name()
        self.id = scraper.get_id()
        self.type = scraper.get_type()
        self.level = scraper.get_level()
        self.description = scraper.get_description()
        self.image = scraper.get_image()
        self.effects = scraper.get_effects()
        self.conditions = scraper.get_conditions()

    def to_json(self) -> dict:
        json = super().to_json()
        json['effects'] = converts_effects_to_dict(self.effects)
        json['conditions'] = self.conditions
        return json
