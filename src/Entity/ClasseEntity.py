from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.dofus.com/fr/mmorpg/encyclopedie/classes/6-ecaflip'

# Configuration du navigateur (dans cet exemple, Chrome)
driver = webdriver.Chrome()  # Assurez-vous que le ChromeDriver est dans le PATH

# Navigation vers la page
driver.get(url)

# Attente pour s'assurer que la page a fini de charger
wait = WebDriverWait(driver, 10)

try:
    # Attendre que l'élément soit chargé et cliquer dessus
    spell = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ak-list-block.ak-spell.ak-spell-selected')))
    
    # Attente explicite pour le nom du sort après avoir cliqué sur l'élément du sort
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ak-spell-name')))

    # Récupérer le nom du sort
    spell_name = driver.find_element(By.CSS_SELECTOR, '.ak-spell-name').text

    # Afficher le nom du sort
    print(spell_name)

except Exception as e:
    print(f"Une erreur s'est produite : {e}")


finally:
    # Fermer le navigateur
    driver.quit()
