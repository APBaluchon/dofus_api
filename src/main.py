from Object.EntityObject import EntityObject
from Scraper.RessourceScraper import RessourceScraper
from Object.RessourceObject import RessourceObject
from Scraper.EntityScraper import EntityScraper
from DAO.filldb import FillDB
from Utils.utils import get_number_pages, get_all_links_from_page, get_all_links
import time

if __name__ == "__main__":
    links = open("src/links/ressources_links.txt", "r").read().split("\n")
    links.pop()
<<<<<<< HEAD
    db = FillDB("dofusdb", "ressources", os.getenv("password"))
    # number_of_created = 0
    # for i, link in enumerate(links):
    #     if (number_of_created+1) % 50 == 0:
    #         time.sleep(60)
    #     print(f"{i+1}/{len(links)}")

    #     id = link.split("/")[-1].split("-")[0]

    #     if not db.id_exists(id):
    #         ressource = RessourceObject(link)
    #         try:
    #             db.insert(ressource)
    #             number_of_created += 1
    #         except:
    #             print(f"Error with {ressource.name}")
    #             continue
    item_1 = RessourceObject("https://www.dofus.com/fr/mmorpg/encyclopedie/ressources/21966-rune-astrale-majeure")
    db.replace(item_1)
    db.close()
=======
    db = FillDB("dofusdb", "ressources")
>>>>>>> 9dcbf234f938a9ae998f75fb30e3b2b67b967a1e

