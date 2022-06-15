import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Ouvrir la fenêtre en plein écran
driver.maximize_window()

# Obtenir l'url de la page
driver.get("https://www.google.com/")

# Faire la recherche
m = driver.find_element(By.NAME, "q")
m.send_keys("selenium")

# Cliquez sur webdriver
driver.find_element(By.XPATH, "//span[. = 'selenium webdriver']").click()

# Fin du programme
time.sleep(3)
driver.quit()