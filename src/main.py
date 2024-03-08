from time import sleep
from Object.EntityObject import EntityObject
from Scraper.RessourceScraper import RessourceScraper
from Object.RessourceObject import RessourceObject
from Object.ConsommableObject import ConsommableObject
from Scraper.ConsommableScraper import ConsommableScraper
from Scraper.EntityScraper import EntityScraper
from Utils import metiers_utils as mu
from DAO.DB import DB
from Utils.utils import get_number_pages, get_all_links_from_page, get_all_links, get_category_content, page_contains_category
from DAO.object_dao import ObjectDao
import os

if __name__ == "__main__":
    db = DB("dofusdb")



    # Fill the database with all the consommables in links/consommables_links.txt
    # ---------------------------------------------------------------------------
    # links = open("src/links/consommables_links.txt", "r").read().split("\n")
    # pbs_links = []
    # nb_inserted = 0
    # for i,link in enumerate(links):
    #     id = link.split("/")[-1].split("-")[0]
    #     print(f"{i}/{len(links)}")
    #     if not db.id_exists(id):
    #         consommable = ConsommableObject(link)
    #         try:
    #             db.insert(consommable)
    #             nb_inserted += 1
    #         except Exception as e:
    #             print(f"Error {i}/{len(links)} : {link}")
    #             print(e)
    #     else:
    #         if db.collection.find_one({"_id": id})["name"] is None:
    #             pbs_links.append(link)
    #     if (nb_inserted+1) % 50 == 0:
    #         print(f"{i} consommables inserted")
    #         sleep(60)
    # print("\n".join(pbs_links))

    # conso = ConsommableObject("https://www.dofus.com/fr/mmorpg/encyclopedie/consommables/16823-tonneau-jus-goutu")
    # db.replace(conso)


    # conso = ConsommableObject("https://www.dofus.com/fr/mmorpg/encyclopedie/consommables/20976-quintessence-bakushana")
    # print(conso.to_json())
    db.insert_with_url("ressources", "https://www.dofus.com/fr/mmorpg/encyclopedie/ressources/2539-substrat-buisson")