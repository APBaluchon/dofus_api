from time import sleep
from Object.EntityObject import EntityObject
from Scraper.RessourceScraper import RessourceScraper
from Object.RessourceObject import RessourceObject
from Object.ConsommableObject import ConsommableObject
from Scraper.ConsommableScraper import ConsommableScraper
from Scraper.EntityScraper import EntityScraper
from Scraper.MontureScraper import MontureScraper
from Utils import metiers_utils as mu
from DAO.DB import DB
from Utils.utils import get_number_pages, get_all_links_from_page, get_all_links, get_category_content, page_contains_category, converts_effects_to_dict
from DAO.ObjectDAO import ObjectDao
import os

if __name__ == "__main__":
    mont = MontureScraper("https://www.dofus.com/fr/mmorpg/encyclopedie/montures/33-dragodinde-amande-doree")
    print(converts_effects_to_dict(mont.get_effects()))