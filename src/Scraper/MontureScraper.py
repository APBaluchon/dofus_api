from Scraper.EntityScraper import EntityScraper
from Utils.utils import get_category_content, page_contains_category

class MontureScraper(EntityScraper):
    def __init__(self, url):
        super().__init__(url)

    def get_effects(self):
        try:
            if self.has_effects():
                effects = get_category_content("Effets", self.soup).find_all('div', class_='ak-title')
                effects = [effect.text.strip() for effect in effects]
                return effects
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None