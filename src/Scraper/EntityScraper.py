from Utils.utils import get_content_page, page_contains_category, get_category_content


class EntityScraper:
    """
    Classe pour récupérer les informations d'une entité du jeu Dofus (Item, Familiers, Montures, ...) à partir de son url.
    """
    def __init__(self, url: str):
        """
        Parameters
        ----------
        url : str
            L'url de l'entité à scraper

        Attributes
        ----------
        url : str
            L'url de l'entité à scraper
        soup : BeautifulSoup
            L'objet soup de la page de l'entité

        Examples
        --------
        >>> url = "https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf"
        >>> item = GameEntity(url)
        """
        self.url = url
        self.soup = get_content_page(self.url)

    def get_name(self) -> str:
        """
        Récupère le nom de l'entité à partir de la page de l'entité.

        Returns
        -------
        str
            Le nom de l'entité

        Examples
        --------
        >>> url = "https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf"
        >>> item = GameEntity(url)
        >>> print(item.get_name())
        """
        try:
            name = self.soup.find("h1", class_='ak-return-link').text.strip()
            return name
        except AttributeError:
            return None
    
    def get_id(self) -> str:
        """
        Récupère l'ID de l'entité à partir de l'URL.

        Returns
        -------
        str
            L'ID de l'entité

        Examples
        --------
        >>> url = "https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf"
        >>> item = GameEntity(url)
        >>> print(item.get_id())
        """
        try:
            entity_id = self.url.split("/")[-1].split("-")[0]
            return entity_id
        except IndexError:
            return None

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
            type = self.soup.find("div", {"class": "ak-encyclo-detail-type"}).get_text().strip().replace("Type : ", "")
            return type
        except AttributeError:
            return None

    def get_level(self) -> str:
        """
        Récupère le niveau de l'entité à partir de la page de l'entité.

        Returns
        -------
        str
            Le niveau de l'entité

        Examples
        --------
        >>> url = "https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf"
        >>> item = GameEntity(url)
        >>> print(item.get_level())
        """
        try:
            level = self.soup.find("div", {"class": "ak-encyclo-detail-level"}).get_text(strip=True).replace("Niveau : ", "").strip()
            return level
        except AttributeError:
            return None

    def get_description(self) -> str:
        """
        Récupère la description de l'entité à partir de la page de l'entité.

        Returns
        -------
        str
            La description de l'entité, ou None si aucune description n'est trouvée.

        Examples
        --------
        >>> url = "https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf"
        >>> item = GameEntity(url)
        >>> print(item.get_description())
        """
        try:
            if page_contains_category("Description", self.soup):
                description_content = get_category_content("Description", self.soup)
                return description_content.get_text().strip()
            return None
        except AttributeError:
            return None
        
    def get_image(self) -> str:
        """
        Récupère l'url de l'image de l'entité à partir de la page de l'entité.

        Returns
        -------
        str
            L'url de l'image de l'entité, ou None si aucune image n'est trouvée.

        Examples
        --------
        >>> url = "https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf"
        >>> item = GameEntity(url)
        >>> print(item.get_image())
        """
        try:
            image = self.soup.find("div", class_='ak-encyclo-detail-illu').find("img")['src']
            return image
        except AttributeError:
            return None
        
    def has_effects(self):
        return page_contains_category("Effets", self.soup)
    
    def has_conditions(self):
        return page_contains_category("Conditions", self.soup)


if __name__ == "__main__":
    url = "https://www.dofus.com/fr/mmorpg/encyclopedie/ressources/13917-cervelle-peunch"
    item = EntityScraper(url)
    print(item.get_name())
    print(item.get_id())
    print(item.get_type())
    print(item.get_level())
    print(item.get_description())
    print(item.get_image())
