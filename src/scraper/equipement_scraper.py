from scraper.entity_scraper import EntityScraper
from utils import utils


class EquipementScraper(EntityScraper):
    """
    Classe pour scraper les informations sur les équipements depuis une URL donnée.

    Args:
        url (str): L'URL de la page à scraper.

    Methods:
        get_effects(): Récupère les effets des équipements depuis la page HTML.
        get_crafts(): Récupère les crafts nécessaires des équipements depuis la page HTML.
        get_panoplie(): Récupère la panoplie à laquelle appartient l'équipenet depuis la page HTML.
    """

    def __init__(self, url: str):
        super().__init__(url)

    def get_effects(self):
        """
        Récupère les effets des équipements depuis la page HTML.

        Returns:
            list or None: Une liste des effets des équipements ou None si aucune information n'est trouvée.
        """
        try:
            if self.has_effects():
                effects = utils.get_category_content("Effets", self.soup).find_all(
                    "div", class_="ak-title"
                )
                effects = [effect.text.strip() for effect in effects]
                return effects
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_crafts(self) -> dict:
        """
        Récupère les crafts nécessaires des équipements depuis la page HTML.

        Returns:
            dict or None: Un dictionnaire représentant les crafts nécessaires des équipements ou None si aucune information n'est trouvée.
        """
        try:
            if utils.page_contains_category("Recette", self.soup):
                items = utils.get_category_content("Recette", self.soup).find_all(
                    "div", class_="ak-title"
                )
                quantities = utils.get_category_content("Recette", self.soup).find_all(
                    "div", class_="ak-front"
                )
                items = [item.text.strip() for item in items]
                quantities = [
                    utils.get_nth_number(quantity.get_text().strip(), 1)
                    for quantity in quantities
                ]

                crafts = {items[i]: quantities[i] for i in range(len(items))}
                return crafts
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_panoplie(self) -> str:
        """
        Récupère la panoplie à laquelle appartient l'équipement depuis la page HTML.

        Returns:
            str or None: Le nom de la panoplie à laquelle appartient l'équipement ou None si aucune information n'est trouvée.
        """
        try:

            titles = self.soup.find_all("div", {"class": "ak-panel-title"})
            panoplie = titles[3].a.get_text().strip()
            return panoplie
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
