from time import sleep
from Object.MontureObject import MontureObject
from Scraper.MontureScraper import MontureScraper
from DAO.DB import DB

if __name__ == "__main__":
    db = DB("dofusdb")
    db.fill("montures")
        
