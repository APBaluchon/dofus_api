from Object.EntityObject import EntityObject
from Scraper.RessourceScraper import RessourceScraper
from Object.RessourceObject import RessourceObject
from Scraper.EntityScraper import EntityScraper
from DAO.filldb import FillDB
from Utils.utils import get_number_pages, get_all_links_from_page, get_all_links
import time

import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    links = open("src/links/ressources_links.txt", "r").read().split("\n")
    links.pop()
    db = FillDB("dofusdb", "ressources", os.getenv("password"))

    for i, link in enumerate(links):
        print(f"{i+1}/{len(links)}")
        ressource = RessourceObject(link)
        if db.exists(ressource):
            print(f"{ressource.name} already in db")
            continue
        else:
            while True:
                try:
                    db.insert(ressource)
                    break
                except:
                    print(f"Error with {ressource.name}")
                    db.insert(ressource)
                    time.sleep(5)
                    continue
        if (i+1) % 50 == 0:
            time.sleep(30)
