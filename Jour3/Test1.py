# Lancer navigateur
# accéder à l'adresse https://demo.nopcommerce.com/
# cliquer sur Register
# Remplir le formulaire
# Cliquer sur Register
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
#Clique sur Register avec le link text
#driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
driver.find_element(By.ID, "FirstName").send_keys("Valentin")
driver.find_element(By.NAME,"LastName").send_keys("De Brito")
driver.find_element(By.ID, "Email").send_keys("adress@gmail.com")
driver.find_element(By.ID,"Password").send_keys("123456")
driver.find_element(By.ID,"register-button").submit()



time.sleep(4)
driver.close()