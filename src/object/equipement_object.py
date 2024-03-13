from object.entity_object import EntityObject
from scraper.equipement_scraper import EquipementScraper
from utils import utils


class EquipementObject(EntityObject):
    def __init__(self, url: str):
        self.effects = []
        self.conditions = []
        super().__init__(url)

    def use_scraper(self):
        scraper = EquipementScraper(self.url)
        self.name = scraper.get_name()
        self.id = scraper.get_id()
        self.type = scraper.get_type()
        self.level = scraper.get_level()
        self.description = scraper.get_description()
        self.image = scraper.get_image()
        self.effects = scraper.get_effects()
        self.panoplie = scraper.get_panoplie()
        self.crafts = scraper.get_crafts()

    def to_json(self) -> dict:
        json = super().to_json()
        json["effects"] = utils.converts_effects_to_dict(self.effects)
        json["crafts"] = self.crafts
        if self.panoplie:
            json["panoplie"] = self.panoplie
        return json
