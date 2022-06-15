import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]").click()





alertWindow = driver.switch_to.alert
print(alertWindow.text)
alertWindow.accept()
time.sleep(3)

driver.quit()
