import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver =webdriver.Chrome(service=serv_chr)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("pra")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
time.sleep(2)
print(len(countries))


for country in countries:
    if country == "India":
        country.click()
        break

# assert print(driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute("value")== "India")
#driver.close()
