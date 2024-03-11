from Scraper.EntityScraper import EntityScraper
from Utils.utils import get_category_content, page_contains_category

class MonstreScraper(EntityScraper):

    def __init__(self, url: str):
        super().__init__(url)
    
    def get_type(self) -> str:
        """
        Récupère le type de l'entité à partir de la page de l'entité.

        Returns
        -------
        str
            Le type de l'entité

        Examples
        --------
        >>> url = "https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf"
        >>> item = GameEntity(url)
        >>> print(item.get_type())
        """
        try:
            type = self.soup.find("div", {"class": "ak-encyclo-detail-type"}).find('span').get_text().strip()
            return type
        except AttributeError:
            return None


if __name__ == "__main__":
    url = "https://www.dofus.com/fr/mmorpg/encyclopedie/monstres/839-abominable-yiti-neiges"
    item = MonstreScraper(url)
    print(item.get_name())
    print(item.get_id())
    print(item.get_type())
    print(item.get_level())
    print(item.get_description())
    print(item.get_image())
