from Object.EntityObject import EntityObject
from Scraper.RessourceScraper import RessourceScraper
from Object.RessourceObject import RessourceObject
from Scraper.EntityScraper import EntityScraper
from DAO.filldb import FillDB
from Utils.utils import get_number_pages, get_all_links_from_page, get_all_links
from DAO.ressources_dao import RessourcesDao

if __name__ == "__main__":
    links = open("links/ressources.txt", "r").read().split("\n")
    links.pop()
    

    for link in links:
        get_id = link.split("/")[-1].split("-")[0]
