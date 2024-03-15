from scraper.entity_scraper import EntityScraper
from utils import utils


class MetierScraper(EntityScraper):
    """
    Cette classe permet de scraper les informations spécifiques à un métier sur un site web.

    Args:
        url (str): L'URL de la page web du métier à scraper.

    Methods:
        get_description() -> str:
            Récupère et retourne la description du métier.

        has_recoltes() -> bool:
            Vérifie si la page contient des informations sur les récoltes du métier.

        has_recettes() -> bool:
            Vérifie si la page contient des informations sur les recettes du métier.

        get_recoltes() -> dict:
            Récupère et retourne un dictionnaire des récoltes du métier avec leur niveau associé.

        get_recettes() -> dict:
            Récupère et retourne un dictionnaire des recettes du métier avec leur niveau associé.
    """

    def __init__(self, url: str):
        super().__init__(url)

    def get_description(self) -> str:
        """
        Récupère la description du métier depuis le contenu de la page Web.

        Returns:
            str: La description du métier.
        """
        desc = (
            self.soup.find("div", class_="ak-panel-content")
            .find("p")
            .get_text(strip=True)
        )
        return desc

    def has_recoltes(self):
        """
        Vérifie si la page contient des informations sur les récoltes.

        Returns:
            bool: True si des récoltes sont présentes, sinon False.
        """
        return utils.page_contains_tab("Récoltes", self.soup)

    def has_recettes(self):
        """
        Vérifie si la page contient des informations sur les recettes.

        Returns:
            bool: True si des recettes sont présentes, sinon False.
        """
        return utils.page_contains_tab("Recettes", self.soup)

    def get_recoltes(self) -> dict:
        """
        Récupère les informations sur les récoltes depuis la page Web.

        Returns:
            dict: Un dictionnaire contenant les récoltes avec leurs niveaux associés.
        """
        if not self.has_recoltes():
            return None
        rows_recolte = self.soup.find("tbody").find_all("tr")
        recoltes = dict()

        for recolte in rows_recolte:
            name = recolte.find_all("td")[1].get_text(strip=True)
            level = recolte.find_all("td")[2].get_text(strip=True)
            recoltes[name] = level

        return recoltes

    def get_recettes(self) -> dict:
        """
        Récupère les informations sur les recettes depuis la page Web.

        Returns:
            dict: Un dictionnaire contenant les recettes avec leurs niveaux associés.
        """
        if not self.has_recettes():
            return None

        end_url = self.url.split("/metiers/")[1]
        nb_pages = utils.get_number_pages(f"metiers/{end_url}")

        all_pages_url = []

        recettes = dict()

        for i in range(nb_pages):
            all_pages_url.append(self.url + f"/recettes?page={i+1}")

        for page_url in all_pages_url:
            soup_recette = utils.get_content_page(page_url)
            if self.has_recoltes() and page_url == all_pages_url[0]:
                rows_recette = soup_recette.find_all("tbody")[1].find_all("tr")
            else:
                rows_recette = soup_recette.find_all("tbody")[0].find_all("tr")

            for recette in rows_recette:
                name = recette.find_all("td")[1].get_text(strip=True)
                level = recette.find_all("td")[2].get_text(strip=True)
                recettes[name] = level

        return recettes
