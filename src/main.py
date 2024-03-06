from Object.EntityObject import EntityObject
from Scraper.RessourceScraper import RessourceScraper
from Object.RessourceObject import RessourceObject
from Object.ConsommableObject import ConsommableObject
from Scraper.ConsommableScraper import ConsommableScraper
from Scraper.EntityScraper import EntityScraper
from Utils import metiers_utils as mu
from DAO.filldb import FillDB
from Utils.utils import get_number_pages, get_all_links_from_page, get_all_links, get_category_content, page_contains_category
from DAO.object_dao import ObjectDao

if __name__ == "__main__":
    #conso = ConsommableObject("https://www.dofus.com/fr/mmorpg/encyclopedie/consommables/13276-poisskaille-givre-ragout")
    #conso_scrap = ConsommableScraper("https://www.dofus.com/fr/mmorpg/encyclopedie/consommables/13276-poisskaille-givre-ragout")
    #print(conso.to_json())

    link = "https://www.dofus.com/fr/mmorpg/encyclopedie/metiers/26-alchimiste"
    test = mu.get_content_metier(link)
    print(test)