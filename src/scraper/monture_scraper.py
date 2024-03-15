from scraper.entity_scraper import EntityScraper
from utils.utils import (
    get_category_content,
    page_contains_category,
    get_content_page,
)


class MontureScraper(EntityScraper):
    """
    Cette classe permet de scraper les informations spécifiques à unu monture sur une page web donnée.

    Args:
        url (str): L'URL de la page web de la monture à scraper.

    Attributes:
        url (str): L'URL de la page web de la monture.

    Methods:
        get_effects_and_caracteristics() -> tuple:
            Récupère les effets et caractéristiques de la monture.
    """
    def __init__(self, url):
        super().__init__(url + "?level=1")

    def get_effects_and_caracteristics(self):
        """
        Récupère les effets et caractéristiques de la monture.

        Returns:
            tuple: Un tuple contenant deux dictionnaires, le premier pour les effets et le second pour les caractéristiques.

        """
        try:
            if self.has_effects() or self.has_caracteristics():
                effects = {}
                caracts = {}
                for i in range(1, 101):
                    self.url = self.url.split("=")[0] + "=" + str(i)
                    self.soup = get_content_page(self.url)
                    print(self.url)
                    if page_contains_category(
                        "Effets", self.soup
                    ) and page_contains_category("Caractéristiques", self.soup):
                        effects[f"level {i}"] = (
                            get_category_content("Effets", self.soup).get_text().strip()
                        )
                        effects[f"level {i}"] = [
                            e.strip()
                            for e in effects[f"level {i}"].split("\n")
                            if e.strip()
                        ]

                        caracts[f"level {i}"] = (
                            get_category_content("Caractéristiques", self.soup)
                            .get_text()
                            .strip()
                        )
                        caracts[f"level {i}"] = [
                            e.strip()
                            for e in caracts[f"level {i}"].split("\n")
                            if e.strip()
                        ]
                    elif page_contains_category("Effets", self.soup):
                        effects[f"level {i}"] = (
                            get_category_content("Effets", self.soup).get_text().strip()
                        )
                        effects[f"level {i}"] = [
                            e.strip()
                            for e in effects[f"level {i}"].split("\n")
                            if e.strip()
                        ]
                    elif page_contains_category("Caractéristiques", self.soup):
                        caracts[f"level {i}"] = (
                            get_category_content("Caractéristiques", self.soup)
                            .get_text()
                            .strip()
                        )
                        caracts[f"level {i}"] = [
                            e.strip()
                            for e in caracts[f"level {i}"].split("\n")
                            if e.strip()
                        ]
                return effects, caracts
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
