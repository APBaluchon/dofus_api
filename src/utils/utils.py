import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def get_content_page(url):
    try:
        response = requests.get(url, headers=headers, timeout = 100000)
    except requests.exceptions.Timeout:
        print("La requête n'a pas pu aboutir.")

    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print("Erreur lors de la récupération de la page")
        return None


def get_name(soup):
    return soup.find("h1", class_='ak-return-link').text.strip()


def get_type(soup):
    return soup.find("div", {"class": "ak-encyclo-detail-type"}).get_text().strip().replace("Type : ", "")


def get_level(soup):
    return soup.find("div", {"class": "ak-encyclo-detail-level"}).get_text(strip=True).replace("Niveau : ", "").strip()


def get_description(soup):
    titles = soup.find_all('div', class_='ak-panel-title')
    for title in titles:
        if "Description" in title.get_text():
            description_content = title.find_next('div', class_='ak-panel-content')
            if description_content:
                return description_content.get_text(strip=True)
    return None


def get_number_pages(cat: str):
    url = "https://www.dofus.com/fr/mmorpg/encyclopedie/" + cat

    soup = get_content_page(url)

    if soup:
        all_opt = soup.find("select", {"class": "ak-select-page"})

        pages = []

        for childdiv in all_opt.find_all('option'):
            pages.append(childdiv.string)

        max_page = 0

        for i in pages:
            try:
                nb = int(i)
                if nb > max_page:
                    max_page = nb
            except ValueError:
                pass
    else:
        max_page = 0

    return max_page



if __name__ == "__main__":
    url = "https://www.dofus.com/fr/mmorpg/encyclopedie/ressources/13921-cuir-cuirboule"
    soup = get_content_page(url)
    if soup:
        description = get_description(soup)
        print(description)
