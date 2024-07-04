import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
Name= "Abhishek Tiwari"
Name1= "Tiwari Abhishek"

serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_chr)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(Name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertxt =alert.text
print(alertxt)
assert Name in alertxt
alert.accept()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(Name1)
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
alerttxt= alert.text
print(alerttxt)
alert.dismiss()

driver.close()