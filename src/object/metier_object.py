from object.entity_object import EntityObject
from scraper.metier_scraper import MetierScraper


class MetierObject(EntityObject):
    """
    Classe représentant un object métier.

    Args:
        url (str): L'URL de l'objet.

    Methods:
        use_scraper(): Utilise un scraper pour extraire les informations de l'objet depuis son URL.
        to_json() -> dict: Convertit l'objet en un dictionnaire JSON.

    """
    def __init__(self, url: str):
        self.drops = dict()
        self.scraper = None
        super().__init__(url)

    def use_scraper(self):
        """
        Utilise un scraper pour extraire les informations de l'objet depuis son URL.
        Met à jour les attributs de l'objet avec les informations extraites.
        """
        self.scraper = MetierScraper(self.url)
        self.name = self.scraper.get_name()
        self.id = self.scraper.get_id()
        self.image = self.scraper.get_image()
        self.desc = self.scraper.get_description()

    def to_json(self) -> dict:
        """
        Convertit l'objet en un dictionnaire JSON.

        Returns:
            dict: Un dictionnaire représentant l'objet sous forme JSON.
        """
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
