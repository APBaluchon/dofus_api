import requests
from bs4 import BeautifulSoup
import os
import re


headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
available_stat = {
    "AGILITÉ": "Agilité",
    "CHANCE": "Chance",
    "FORCE": "Force",
    "INTELLIGENCE": "Intelligence",
    "SAGESSE": "Sagesse",
    "APPLIQUE UN BONUS": "Bonus",
    "CRAFT COOPÉRATIF IMPOSSIBLE": "Malus",
    "ÉNERGIE": "Energie",
    "VIE": "Vie",
    "INITIATIVE": "Initiative",
    "VITALITÉ": "Vitalité",
    "INVOCATION": "Invocation",
    "TACLE": "Tacle",
    "SOIN": "Soin",
    "RÉSISTANCE POUSSÉE": "Résistance poussée",
    "% CRITIQUE": "% Critique",
    "% RÉSISTANCE AIR": "% Résistance Air",
    "% RÉSISTANCE EAU": "% Résistance Eau",
    "% RÉSISTANCE FEU": "% Résistance Feu",
    "% RÉSISTANCE NEUTRE": "% Résistance Neutre",
    "% RÉSISTANCE TERRE": "% Résistance Terre",
    "DOMMAGES CRITIQUES": "Dommages Critiques",
    "DOMMAGES POUSSÉE": "Dommages Poussée",
    "ESQUIVE PA": "Esquive PA",
    "ESQUIVE PM": "Esquive PM",
    "FUITE": "Fuite",
    "INVOCATIONS": "Invocations",
    "PA": "PA",
    "PM": "PM",
    "PORTÉE": "Portée",
    "PROSPECTION": "Prospection",
    "PUISSANCE": "Puissance",
    "RENVOIE DOMMAGE": "Renvoie Dommage",
    "RETRAIT PA": "Retrait PA",
    "RETRAIT PM": "Retrait PM",
    "RÉSISTANCE CRITIQUES": "Résistance Critiques",
    "RÉSISTANCE POUSSÉE": "Résistance Poussée",
    "SOINS": "Soins",
}

caracteristiques = {
    "GÉNÉRATION": "Génération",
    "NOMBRE DE PODS": "Nombre de pods",
    "TEMPS DE GESTATION": "Temps de gestation",
    "MATURITÉ": "Maturité",
    "ENERGIE": "Energie",
    "VITESSE": "Vitesse",
    "VITESSE DE DÉPLACEMENT": "Vitesse de déplacement",
    "TAUX D'APPRENTISAGE": "Taux d'apprentisage",
    "CAPTURABLE": "Capturable"
}

stats_without_number = ["Bonus", "Malus"]

def get_content_page(url: str) -> BeautifulSoup:
    """
    Récupère le contenu de la page de l'entité et le stocke dans l'attribut soup.
       
    Examples
    --------
    >>> url = "https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf"
    >>> item = GameEntity(url)
    >>> print(item.soup)
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def get_number_pages(cat: str) -> int:
    """
    Récupère le nombre de pages disponibles pour une catégorie donnée.

    Parameters
    ----------
    cat : str
        La catégorie pour laquelle on souhaite récupérer le nombre de pages.

    Returns
    -------
    int
        Le nombre de pages disponibles pour la catégorie donnée.

    Examples
    --------
    >>> get_number_pages("familiers")
    6
    """
    url = "https://www.dofus.com/fr/mmorpg/encyclopedie/" + cat

    soup = get_content_page(url)

    if soup:
        all_opt = soup.find("ul", {"class": "ak-pagination pagination ak-ajaxloader"})

        pages = [int(childdiv.string) for childdiv in all_opt.find_all('a') if childdiv.string.isdigit()]

        max_page = max(pages) if pages else 0
    else:
        max_page = 0

    return max_page

def get_all_links_from_page(cat: str, page: int) -> list:
    """
    Récupère tous les liens des entités d'une catégorie donnée pour une page donnée.

    Parameters
    ----------
    cat : str
        La catégorie pour laquelle on souhaite récupérer les liens.
    page : int
        Le numéro de la page pour laquelle on souhaite récupérer les liens.

    Returns
    -------
    list
        La liste des liens des entités de la catégorie donnée pour la page donnée.

    Examples
    --------
    >>> get_all_links_from_page("familiers", 1)
    ['https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf', 'https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12542-dragoune', ...]
    """
    url = "https://www.dofus.com/fr/mmorpg/encyclopedie/" + cat + "?page=" + str(page)

    soup = get_content_page(url)

    if soup:
        all_links = soup.find_all("span", {"class": "ak-linker"})

        links = []
        for link in all_links:
            try:
                links.append(link.a['href'])
            except TypeError:
                pass
        links = set(["https://www.dofus.com" + link for link in links])
    else:
        links = []

    return links

def get_all_links(cat: str, filepath: str = None, starting_page: int = 1, nb_page: int = None) -> None:
    """
    Récupère tous les liens des entités d'une catégorie donnée.

    Parameters
    ----------
    cat : str
        La catégorie pour laquelle on souhaite récupérer les liens.
    filepath : str
        Le chemin du fichier dans lequel on souhaite stocker les liens.

    Examples
    --------
    >>> get_all_links("familiers")
    ['https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12541-dragouf', 'https://www.dofus.com/fr/mmorpg/encyclopedie/familiers/12542-dragoune', ...]
    """
    if not nb_page:
        nb_page = get_number_pages(cat)

    links = []

    for i in range(starting_page, nb_page + 1):
        print(f"Page {i}/{nb_page}")
        links += get_all_links_from_page(cat, i)

    if filepath:
        open(filepath, 'w').close()
        with open(filepath, 'w') as file:
            for link in links:
                file.write(link + '\n')

def page_contains_category(cat: str, soup: BeautifulSoup) -> bool:
    titles = soup.find_all('div', class_='ak-panel-title')
    for title in titles:
        if cat in title.get_text():
            return True
    return False

def page_contains_tab(cat: str, soup: BeautifulSoup) -> bool:
    titles = soup.find_all('div', class_='ak-container ak-tabs-container')
    for title in titles:
        if cat in title.get_text():
            return True
    return False

def get_category_content(cat: str, soup: BeautifulSoup):
    titles = soup.find_all('div', class_='ak-panel-title')
    for title in titles:
        if cat in title.get_text():
            cat_content = title.find_next('div', class_='ak-panel-content')
            return cat_content
    return None

def converts_effects_to_dict(effects: list) -> dict:
    dict_effects = {}
    if effects is not None:
        for effect in effects:
            effect.replace("{~ps}{~zs}", "")
            if "+" in effect:
                stat = find_good_stat(effect)
                dict_effects[stat] = get_nth_number(effect, 1)
            else:
                if "à" in effect:
                    stat = find_good_stat(effect)
                    dict_effects[stat] = {
                        "from": get_nth_number(effect, 1),
                        "to": get_nth_number(effect, 2)
                    }
                else:
                    stat = find_good_stat(effect)
                    if stat in stats_without_number:
                        dict_effects[stat] = effect
                    else:
                        dict_effects[stat] = get_nth_number(effect, 1)
            
    return dict_effects

def converts_caracteristics_to_dict(caracteristics: list) -> dict:
    caracteristics_dict = {}
    if caracteristics is not None:
        for caract in caracteristics:
            caracteristic = find_good_caracteristic(caract)
            if contains_number(caract):
                caracteristics_dict[caracteristic] = get_nth_number(caract, 1)
            else:
                if "Non" in caract:
                    caracteristics_dict[caracteristic] = "Non"
                elif "Oui" in caract:
                    caracteristics_dict[caracteristic] = "Oui"
    return caracteristics_dict

def get_nth_number(s: str, n: int) -> int:
    numbers = [int(num) for num in re.findall(r'-?\d+', s)]
    return numbers[n - 1] if len(numbers) >= n else 0


def contains_number(s: str) -> bool:
    return any(char.isdigit() for char in s)

def find_good_stat(s: str) -> str:
    for stat in available_stat:
        if stat in s.upper():
            return available_stat[stat]
        
def find_good_caracteristic(s: str) -> str:
    for caract in caracteristiques:
        if caract in s.upper():
            return caracteristiques[caract]
        
def add_spaces(s: str) -> str:
    s = s.replace("+", "+ ")
    s = s.replace("-", "- ")
    return s

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

    soup = get_content_page(url)

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
        open(filepath, 'w').close()
        with open(filepath, 'w') as file:
            for link in links:
                file.write(link + '\n')
