from Object.EntityObject import EntityObject
from Scraper.RessourceScraper import RessourceScraper

class RessourceObject(EntityObject):
    """
    Répresente une ressource du jeu
    """
    def __init__(self, url: str):
        """
        Initialise une ressource

        Parameters
        ----------
        url : str
            L'url de la ressource

        Attributes
        ----------
        name : str
            Le nom de la ressource
        id : str
            L'ID de la ressource
        type : str
            Le type de la ressource
        level : str
            Le niveau de la ressource
        description : str
            La description de la ressource
        image : str
            L'image de la ressource
        """
        super().__init__(url)
        
    def use_scraper(self):
        """
        Utilise un scraper pour récupérer les informations de la ressource.
        """
        scraper = RessourceScraper(self.url)
        self.name = scraper.get_name()
        self.id = scraper.get_id()
        self.type = scraper.get_type()
        self.level = scraper.get_level()
        self.description = scraper.get_description()
        self.image = scraper.get_image()