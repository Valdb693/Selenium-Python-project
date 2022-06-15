import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")
countySelect=driver.find_element(By.NAME, "country_id")

country=Select(countySelect)
#country.select_by_visible_text("Canada")
#country.select_by_index(1)
country.select_by_value("3")
# Récupérer toutes les options dans select
toutesOptions=country.options
total_option=len(toutesOptions)
print("Le nombre des options", total_option)

# for opt in toutesOptions:
#     print(opt.text)
for opt in toutesOptions:
    print(opt.text)
    if opt.text=="Canada":

        opt.click()
        break


time.sleep(2)
driver.close()