import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
promptWindow=driver.switch_to.alert

text_input=("Bonjour Rabah")

promptWindow.send_keys(text_input)
time.sleep(2)
promptWindow.accept()

act_text = driver.find_element(By.ID,'result').text
exp_text = ("You entered: "+text_input)

if act_text == exp_text:
    print("Le test prompt est passed")
else:
  print("Le test prompt  est failed")





time.sleep(3)
driver.close()