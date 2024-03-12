from time import sleep
from Object.MontureObject import MontureObject
from Scraper.MontureScraper import MontureScraper
from DAO.DB import DB
from Scraper.MonstreScraper import MonstreScraper
from Object.MonstreObject import MonstreObject
from Utils.utils import get_nth_number

if __name__ == "__main__":
    monstre = MonstreObject("https://www.dofus.com/fr/mmorpg/encyclopedie/monstres/650-abrakne")
    print(monstre.to_json())
        
