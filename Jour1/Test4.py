#Test Case
#------------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://login.salesforce.com/#
# 3) Entrer username (arwa)
# 4) Entrer password (arwa)
# 5) Cliquer sur le bouton Se connecter
# 6) recuperer le titre de la page(titre actuel)
# 7) Verifier le titre de la page: Connexion | Salesforce  (attendu)
# 8) Fermer le navigateur
import time

from selenium.webdriver.chrome.service import  Service
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome()
# 2) Naviguer vers l'url https://login.salesforce.com/
driver.get("https://login.salesforce.com//")
driver.maximize_window()
# 3) Entrer username (Admin)
driver.find_element(By.ID, "username").send_keys("arwa")
# 4) Entrer password (admin123)
driver.find_element(By.ID, "password").send_keys("arwa")
# 5) Cliquer sur le bouton Login
driver.find_element(By.ID, "Login").click()
# 6) recuperer le titre de la page(titre actuel)
act_title =  driver.title
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
exp_title = "Connexion | Salesforce"
if act_title == exp_title:
    print("Le test Login  est passed")
else:
    print("Le test Login  est failed")
    time.sleep(4)  # Temporisateur (synchronisation)
    # 8) Fermer le navigateur
    driver.close()


