from scraper.entity_scraper import EntityScraper
from utils.utils import get_category_content


class ConsommableScraper(EntityScraper):
    """
    Classe pour scraper les informations sur les consommables depuis une URL donnée.

    Args:
        url (str): L'URL de la page à scraper.

    Methods:
        get_effects(): Récupère les effets des consommables depuis la page HTML.
        get_conditions(): Récupère les conditions des consommables depuis la page HTML.
    """

    def __init__(self, url: str):
        super().__init__(url)

    def get_effects(self) -> list:
        """
        Récupère les effets des consommables depuis la page HTML.

        Returns:
            list: Une liste contenant les effets des consommables, ou None si aucune information n'est trouvée.
        """
        try:
            if self.has_effects():
                effects = get_category_content("Effets", self.soup).find_all(
                    "div", class_="ak-title"
                )
                effects = [effect.text.strip() for effect in effects]
                return effects
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_conditions(self) -> list:
        """
        Récupère les conditions des consommables depuis la page HTML.

        Returns:
            list: Une liste contenant les conditions des consommables, ou une liste vide si aucune information n'est trouvée.
        """
        try:
            if self.has_conditions():
                conditions = get_category_content("Conditions", self.soup).find_all(
                    "div", class_="ak-title"
                )
                if conditions:
                    conditions = [condition.text.strip() for condition in conditions]
                    return conditions
            else:
                return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
