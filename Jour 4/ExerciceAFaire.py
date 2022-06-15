
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome()
driver.maximize_window()
# 2) Naviguer vers l'url
driver.get("https://www.saucedemo.com/")
# 3) Entrer username (Admin)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
# 4) Entrer password (admin123)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
# 5) Se connecter
driver.find_element(By.ID, "login-button").submit()
# 6) Sélectionner un article
driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack").click()
# 7) Mettre l'article dans le panier
driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
# 8) Aller voir le panier
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
# 9) Vider le panier
driver.find_element(By.NAME, "remove-sauce-labs-backpack").click()
# 10) Laisser ouvert 4 secondes
time.sleep(4)
# 11) Fermer le navigateur
driver.close()