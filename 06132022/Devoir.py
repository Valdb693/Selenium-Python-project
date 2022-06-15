
import time

from selenium import webdriver
from selenium.webdriver.common.by import By




from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# 2) Naviguer vers l'url http://omayo.blogspot.com/
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()

marqueAuto=driver.find_element(By.ID, "multiselect1")

marque=Select(marqueAuto)
marque.select_by_value("audix")

time.sleep(3)
# 8) Fermer le navigateur
driver.close()
