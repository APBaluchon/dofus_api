from Scraper.EntityScraper import EntityScraper
from Utils import utils

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
    
    def get_level(self) -> dict:
        """
        Récupère le niveau de l'entité à partir de la page de l'entité.

        Returns
        -------
        dict
            Les niveaux min et max du monstre
        """
        try:
            level = self.soup.find("div", {"class": "ak-encyclo-detail-level"}).get_text(strip=True).replace("Niveau : ", "").strip()
            
            levels = dict()

            levels["min"] = utils.get_nth_number(level, 1)
            levels["max"] = utils.get_nth_number(level, 2)

            return levels
        except AttributeError:
            return None

    def get_image(self) -> str:
        """
        Récupère l'url de l'image de l'entité à partir de la page de l'entité.

        Returns
        -------
        str
            L'url de l'image de l'entité, ou None si aucune image n'est trouvée.
        """
        try:
            image = self.soup.find("div", class_='ak-encyclo-detail-illu').find("img")['data-src']
            return image
        except AttributeError:
            return None

    def get_drops(self) -> dict:
        """
        Récupère les drops et le pourcentage de drop pour un monstre donné.

        Returns
        -------
        dict
            Un dictionnaire contenant l'item drop et son pourcentage de chance de drop
        """
        try:
            drops_html = self.soup.find_all("div", {"id": 'ak-encyclo-monster-drops ak-container ak-content-list'})

            drops = dict()

            for drop in drops_html:
                name_item = drop.find("div", class_='ak-title').get_text().strip()
                drop_percent = drop.find("div", class_='ak-drop-percent').get_text().strip()

            
                drops[name_item] = drop_percent
            

            return drops
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
