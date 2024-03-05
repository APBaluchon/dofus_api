import requests
from bs4 import BeautifulSoup
import os

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

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
        all_opt = soup.find("select", {"class": "ak-select-page"})

        pages = [int(childdiv.string) for childdiv in all_opt.find_all('option') if childdiv.string.isdigit()]

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

        links = [link.a['href'] for link in all_links]
        links = set(["https://www.dofus.com" + link for link in links])
    else:
        links = []

    return links

def get_all_links(cat: str, filepath: str = None, starting_page: int = 1) -> None:
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
    if filepath:
        if os.path.exists(filepath):
            if starting_page == 1:
                f = open(filepath, "w")
                f.close()
        else:
            open(filepath, 'x').close()
            
    nb_page = get_number_pages(cat)

    links = []
    for i in range(starting_page, nb_page + 1):
        links += get_all_links_from_page(cat, i)

    if filepath:
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filepath, 'w') as file:
            for link in links:
                file.write(link + '\n')
    