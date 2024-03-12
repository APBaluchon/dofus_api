from Scraper.EntityScraper import EntityScraper
from Utils import utils

class EquipementScraper(EntityScraper):

    def __init__(self, url: str):
        super().__init__(url)

    def get_effects(self):
        try:
            if self.has_effects():
                effects = utils.get_category_content("Effets", self.soup).find_all('div', class_='ak-title')
                effects = [effect.text.strip() for effect in effects]
                return effects
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_crafts(self) -> dict:
        try:
            if utils.page_contains_category("Recette", self.soup):
                items = utils.get_category_content("Recette", self.soup).find_all('div', class_='ak-title')
                quantities = utils.get_category_content("Recette", self.soup).find_all('div', class_='ak-front')
                items = [item.text.strip() for item in items]
                quantities = [utils.get_nth_number(quantity.get_text().strip(), 1) for quantity in quantities]

                crafts = {items[i]: quantities[i] for i in range(len(items))}
                return crafts
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    


    def get_panoplie(self) -> str:
        try:
            
            titles = self.soup.find_all("div", {"class": "ak-panel-title"})
            panoplie = titles[3].a.get_text().strip()
            return panoplie
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
