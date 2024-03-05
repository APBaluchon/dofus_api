from Scraper.EntityScraper import EntityScraper

class RessourceScraper(EntityScraper):
    def __init__(self, url: str):
        """
        Initialise une instance de RessourceScraper.

        Parameters:
        ----------
            url (str): L'URL de la ressource.
        """
        super().__init__(url)

if __name__ == "__main__":
    url = "https://www.dofus.com/fr/mmorpg/encyclopedie/ressources/13917-cervelle-peunch"
    item = RessourceScraper(url)
    print(item.get_name())
    print(item.get_id())
    print(item.get_type())
    print(item.get_level())
    print(item.get_description())
    print(item.get_image())