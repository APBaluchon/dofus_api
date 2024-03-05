from Object.EntityObject import EntityObject
from Scraper.RessourceScraper import RessourceScraper
from Object.RessourceObject import RessourceObject
from Scraper.EntityScraper import EntityScraper
from DAO.filldb import FillDB
from Utils.utils import get_number_pages, get_all_links_from_page, get_all_links
from DAO.object_dao import ObjectDao

if __name__ == "__main__":
    # get all links
    # -------------
    # get_all_links("ressources", "src/links/all_ressources.txt")
    
    db = FillDB("dofusdb", "ressources")
    dao = ObjectDao("ressources")

    # find missing links
    # -------------------
    # links = open("src/links/all_ressources.txt", "r").read().split("\n")
    # links.pop()
    # for i,link in enumerate(links):
    #     id = link.split("/")[-1].split("-")[0]
    #     if not db.id_exists(id):
    #         missing_links = open("src/links/missing_ressources.txt", "w")
    #         missing_links.write(link + "\n")

    # fill db with missing links
    # ---------------------------
    # links = open("src/links/missing_ressources.txt", "r").read().split("\n")
    # links.pop()
    # for i,link in enumerate(links):
    #     id = link.split("/")[-1].split("-")[0]
    #     if not db.id_exists(id):
    #         print(f"{i}/{len(links)}")
    #         ressource = RessourceObject(link)
    #         db.insert(ressource)
    #         print(f"Inserted {ressource.name}")

    # find element with none in db
    # -----------------------------
    # links = open("src/links/all_ressources.txt", "r").read().split("\n")
    # links.pop()
    # for i,link in enumerate(links):
    #     id = link.split("/")[-1].split("-")[0]
    #     if db.id_exists(id):
    #         ressource = db.collection.find_one({"_id": id})     
    #         if ressource["type"] == None:
    #             print(f"{i}/{len(links)}")
    #             ressource = RessourceObject(link)
    #             db.replace(ressource)
    #             print(f"Replaced {ressource.name}")
            