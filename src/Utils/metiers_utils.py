import requests
import re
from bs4 import BeautifulSoup
from Utils import utils as ut
import os

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def get_all_links_from_page_metiers(page: int) -> set:
    """
    Récupère tous les liens des entités de la catégorie métiers pour une page donnée.

    Parameters
    ----------
    page : int
        Le numéro de la page pour laquelle on souhaite récupérer les liens.

    Returns
    -------
    list
        La liste des liens des entités de la catégorie métiers pour la page donnée.

    Examples
    --------
    >>> get_all_links_from_page_metiers(1)
    {'https://www.dofus.com/fr/mmorpg/encyclopedie/metiers/45-forgemage-marteaux', 'https://www.dofus.com/fr/mmorpg/encyclopedie/metiers/31-forgeur-haches', ...}
    """
    url = "https://www.dofus.com/fr/mmorpg/encyclopedie/metiers" + "?page=" + str(page)

    soup = ut.get_content_page(url)

    if soup:
        all_links = soup.find_all("div", {"class": "ak-mosaic-item-name"})

        links = [link.a['href'] for link in all_links]
        links = set(["https://www.dofus.com" + link for link in links])
    else:
        links = []

    return links

def get_all_links_metiers(filepath: str = None, starting_page: int = 1) -> None:
    """
    Récupère tous les liens des entités de la catégorie métier.

    Parameters
    ----------
    filepath : str
        Le chemin du fichier dans lequel on souhaite stocker les liens.

    Examples
    --------
    >>> get_all_links_metiers(")
    ['https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf', 'https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12542-dragoune', ...]
    """
    if filepath:
        if os.path.exists(filepath):
            if starting_page == 1:
                f = open(filepath, "w")
                f.close()
        else:
            open(filepath, 'x').close()

    nb_page = 2

    links = []
    for i in range(starting_page, nb_page + 1):
        links += get_all_links_from_page_metiers(i)

    if filepath:
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filepath, 'w') as file:
            for link in links:
                file.write(link + '\n')

def get_content_metier(url: str):
    soup = ut.get_content_page(url)

    metier_content = None

    if soup:
        id = ''.join(re.findall(r'\d', url))

        title = soup.find("h1", {"class": "ak-return-link"}).get_text(strip=True)

        desc = soup.find('div', class_='ak-panel-content').find('p').get_text(strip=True)

        img_link = soup.find('div', class_='ak-encyclo-detail-illu').find('img')['src']

        rows_recolte = soup.find('tbody').find_all('tr')

        recoltes = dict()

        for recolte in rows_recolte:
            name = recolte.find_all('td')[1].get_text(strip=True)
            level = recolte.find_all('td')[2].get_text(strip=True)
            recoltes[name] = level
        
        rows_recette = soup.find_all('tbody')[1].find_all('tr')

        recettes = dict()        

        for recette in rows_recette:
            name = recette.find_all('td')[1].get_text(strip=True)
            level = recette.find_all('td')[2].get_text(strip=True)
            recettes[name] = level
        
        metier_content = {"id": id, "name": title, "description": desc, "image": img_link, "recoltes": recoltes, "recette": recettes}

    return metier_content