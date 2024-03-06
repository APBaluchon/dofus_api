from Scraper.EntityScraper import EntityScraper
from Utils.utils import get_category_content, page_contains_category

class ConsommableScraper(EntityScraper):

    def __init__(self, url: str):
        super().__init__(url)

    def has_effects(self):
        return page_contains_category("Effets", self.soup)

    def get_effects(self):
        if self.has_effects():
            effects = get_category_content("Effets", self.soup).find_all('div', class_='ak-title')
            effects = [effect.text.strip() for effect in effects]
            return effects
        else:
            return None
        
    def has_condition(self):
        return page_contains_category("Conditions", self.soup)
    
    def get_conditions(self):
        if self.has_condition():
            conditions = get_category_content("Conditions", self.soup).find_all('div', class_='ak-title')
            conditions = [condition.text.strip() for condition in conditions]
            return conditions
        else:
            return None