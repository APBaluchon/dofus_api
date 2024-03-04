import requests
from bs4 import BeautifulSoup

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

if __name__ == "__main__":
    print(get_number_pages("familiers"))