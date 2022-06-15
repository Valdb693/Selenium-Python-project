import time

from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import  Service


#service_obj = Service("C:\\Users\\valdb\\Desktop\\Drivers\\chromedriver.exe")

# Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome()
# 2) Naviguer vers l'url https://google.com/
driver.get("https://google.com/")
driver.maximize_window()

driver.find_element(By.XPATH)


time.sleep(3)
# 8) Fermer le navigateur
driver.close()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By