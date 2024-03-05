from Scraper.EntityScraper import EntityScraper


class EntityObject:
    """
    Répresente une entité du jeu
    """
    def __init__(self, url: str):
        """

        Parameters
        ----------
        url : str
            L'url de l'entité

        Attributes
        ----------
        name : str
            Le nom de l'entité
        id : str
            L'ID de l'entité
        type : str
            Le type de l'entité
        level : str
            Le niveau de l'entité
        description : str
            La description de l'entité
        image : str
            L'image de l'entité
            
        Examples
        --------
        >>> url = "https://www.dofus.com/fr/mmorpg/encyclopedie/ressources/13917-cervelle-peunch"
        >>> item = EntityObject(url)
        """
        self.name = None
        self.id = None
        self.type = None
        self.level = None
        self.description = None
        self.image = None
        self.url = url
        self.use_scraper()

    def use_scraper(self):
        """
        Utilise un scraper pour récupérer les informations de l'entité.
        """
        scraper = EntityScraper(self.url)
        self.name = scraper.get_name()
        self.id = scraper.get_id()
        self.type = scraper.get_type()
        self.level = scraper.get_level()
        self.description = scraper.get_description()
        self.image = scraper.get_image()

    def to_json(self) -> dict:
        """
        Convertit l'entité en un dictionnaire JSON.

        Returns
        -------
        dict
            L'entité sous forme de dictionnaire JSON
        """
        return {
            "name": self.name,
            "_id": self.id,
            "type": self.type,
            "level": self.level,
            "description": self.description,
            "image": self.image
        }