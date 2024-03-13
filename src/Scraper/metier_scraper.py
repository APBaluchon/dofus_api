from scraper.entity_scraper import EntityScraper
from utils import utils


class MetierScraper(EntityScraper):

    def __init__(self, url: str):
        super().__init__(url)

    def get_description(self) -> str:
        desc = (
            self.soup.find("div", class_="ak-panel-content")
            .find("p")
            .get_text(strip=True)
        )
        return super().get_description()

    def has_recoltes(self):
        return utils.page_contains_tab("Récoltes", self.soup)

    def has_recettes(self):
        return utils.page_contains_tab("Recettes", self.soup)

    def get_recoltes(self) -> dict:
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
