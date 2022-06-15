import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
# Mettre le driver dans une variable
parentWindowsId = driver.current_window_handle

# Identifiant de la 1er fenêtre : CDwindow-83DF2B42917A8396A692FB2849440320
print(parentWindowsId)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
# Récupère un seul id de fenêtre
#driver.current_window_handle
# Récupère la liste des ids de fenêtre ouvertes
windowsHandlelsIds =driver.window_handles
# 1 ere fenêtre
parentWindowsId = windowsHandlelsIds[0]
# 2eme fenêtre
childWindowId = windowsHandlelsIds[1]
# les ids genérés sont dynamiques
print("parentWindowsId : ", parentWindowsId)
print("childWindow : ", childWindowId)

url1 = driver.current_url
title1 = driver.title
print(url1)
print(title1)

# 2eme approche : parcourir la liste de windowsHandleIds et vrf le titre
for winId in windowsHandlelsIds:
    driver.switch_to.window(winId)
    if driver.title == title1 :
        driver.close()

time.sleep(2)
driver.quit()