from object.entity_object import EntityObject
from scraper.consommable_scraper import ConsommableScraper
from utils.utils import converts_effects_to_dict


class ConsommableObject(EntityObject):
    """
    Classe représentant un objet consommable.

    Args:
        url (str): L'URL de l'objet.

    Methods:
        use_scraper(): Utilise un scraper pour extraire les informations de l'objet depuis son URL.
        to_json() -> dict: Convertit l'objet en un dictionnaire JSON.

    """
    def __init__(self, url: str):
        self.effects = []
        self.conditions = []
        super().__init__(url)

    def use_scraper(self):
        """
        Utilise un scraper pour extraire les informations de l'objet depuis son URL.
        Met à jour les attributs de l'objet avec les informations extraites.
        """
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
        """
        Convertit l'objet en un dictionnaire JSON.

        Returns:
            dict: Un dictionnaire représentant l'objet sous forme JSON.
        """
        json = super().to_json()
        json["effects"] = converts_effects_to_dict(self.effects)
        json["conditions"] = self.conditions
        return json
