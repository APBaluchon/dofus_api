from scraper.entity_scraper import EntityScraper
from utils.utils import get_category_content


class ConsommableScraper(EntityScraper):

    def __init__(self, url: str):
        super().__init__(url)

    def get_effects(self):
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

    def get_conditions(self):
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
