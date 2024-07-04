import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_chr)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radiobutons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
print(len(radiobutons))

for radio in radiobutons:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        break

radiobutons[2].click()
assert radiobutons[2].is_selected()

assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[id='hide-textbox']").click()
time.sleep(2)
assert not driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
driver.find_element(By.ID,"show-textbox").click()

assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()