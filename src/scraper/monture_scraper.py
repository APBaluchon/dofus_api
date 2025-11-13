import logging

from scraper.entity_scraper import EntityScraper
from utils.utils import get_category_content, page_contains_category, get_content_page


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
        effects: dict[str, list[str]] = {}
        caracts: dict[str, list[str]] = {}

        try:
            if not (self.has_effects() or self.has_caracteristics()):
                return effects, caracts

            base_url = self.url.split("?")[0]

            for level in range(1, 101):
                page_url = f"{base_url}?level={level}"
                soup = get_content_page(page_url)
                if not soup or soup == "404":
                    break

                self.soup = soup

                has_effects = page_contains_category("Effets", self.soup)
                has_caracts = page_contains_category("Caractéristiques", self.soup)

                if not has_effects and not has_caracts:
                    break

                if has_effects:
                    raw_effects = get_category_content("Effets", self.soup).get_text().strip()
                    effects[f"level {level}"] = [
                        entry.strip()
                        for entry in raw_effects.split("\n")
                        if entry.strip()
                    ]

                if has_caracts:
                    raw_caracts = (
                        get_category_content("Caractéristiques", self.soup)
                        .get_text()
                        .strip()
                    )
                    caracts[f"level {level}"] = [
                        entry.strip()
                        for entry in raw_caracts.split("\n")
                        if entry.strip()
                    ]

            return effects, caracts
        except Exception as err:  # pragma: no cover - scraping dépend du réseau
            logging.error("Error while scraping mount data %s: %s", self.url, err)
            return effects, caracts
