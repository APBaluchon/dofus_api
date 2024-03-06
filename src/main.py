from Object.EntityObject import EntityObject
from Scraper.RessourceScraper import RessourceScraper
from Object.RessourceObject import RessourceObject
from Scraper.ConsommableScraper import ConsommableScraper
from Scraper.EntityScraper import EntityScraper
from DAO.filldb import FillDB
from Utils.utils import get_number_pages, get_all_links_from_page, get_all_links, get_category_content, page_contains_category
from DAO.object_dao import ObjectDao

if __name__ == "__main__":
    conso = RessourceScraper("https://www.dofus.com/fr/mmorpg/encyclopedie/ressources/13917-cervelle-peunch")
    obj = RessourceObject("https://www.dofus.com/fr/mmorpg/encyclopedie/ressources/13917-cervelle-peunch")
    print(conso.get_description())
    print(obj.description)