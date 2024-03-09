from time import sleep
from Object.MontureObject import MontureObject
from Scraper.MontureScraper import MontureScraper
from DAO.DB import DB

if __name__ == "__main__":
    db = DB("dofusdb")
    link = open("src/links/link_montures.txt", "r").read().split("\n")
    for l in link:
        monture = MontureObject(l)
        db.insert_entity("montures", monture)
        sleep(120)
        
