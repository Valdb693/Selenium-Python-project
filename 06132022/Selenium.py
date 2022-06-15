import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH,"//a/span[text()='WebDriver']").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH,"//a/span[text()='WebDriver']").click()


time.sleep(3)

driver.quit()
