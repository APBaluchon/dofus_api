from scraper.entity_scraper import EntityScraper


class RessourceScraper(EntityScraper):
    def __init__(self, url: str):
        """
        Initialise une instance de RessourceScraper.

        Parameters:
        ----------
            url (str): L'URL de la ressource.
        """
        super().__init__(url)
