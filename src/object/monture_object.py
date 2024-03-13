from object.entity_object import EntityObject
from scraper.monture_scraper import MontureScraper
from utils.utils import converts_effects_to_dict, converts_caracteristics_to_dict


class MontureObject(EntityObject):
    def __init__(self, url: str):
        self.effects = []
        self.caracteristics = []
        super().__init__(url)

    def use_scraper(self):
        scraper = MontureScraper(self.url)
        self.name = scraper.get_name()
        self.id = scraper.get_id()
        self.effects, self.caracteristics = scraper.get_effects_and_caracteristics()
        if self.effects is not None:
            for effect in self.effects:
                self.effects[effect] = converts_effects_to_dict(self.effects[effect])
        if self.caracteristics is not None:
            for caract in self.caracteristics:
                self.caracteristics[caract] = converts_caracteristics_to_dict(
                    self.caracteristics[caract]
                )

    def to_json(self) -> dict:
        return {
            "_id": self.id,
            "name": self.name,
            "effects": self.effects,
            "caracteristics": self.caracteristics,
        }
