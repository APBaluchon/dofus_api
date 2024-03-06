from Scraper.EntityScraper import EntityScraper

class ConsommableScraper(EntityScraper):

    def __init__(self, url: str):
        super().__init__(url)

    def has_effects(self):
        all_divs_titles = self.soup.find_all('div', class_='ak-panel-title')
        print("Description" in all_divs_titles[0].text)