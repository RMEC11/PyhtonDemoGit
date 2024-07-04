import time

from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.embibe.com/")
driver.maximize_window()
print(driver.current_url)
time.sleep(10)
driver.find_element(By.ID, "wzrk-cancel").click()
driver.find_element(By.XPATH, "//button[@class='eds-btn eds-btn--primary eds-btn--capsular eds-btn--md']").click()
time.sleep(2)
sign_up = driver.current_url
print(sign_up)
time.sleep(1)
driver.find_element(By.XPATH, "//input[@class='eds-text-field css-efet9v']").send_keys("abhishek.tiwari@embibe.com")
time.sleep(5)
driver.find_element(By.XPATH,"")
#driver.find_element(By.XPATH, "//button[@class='eds-btn eds-btn--secondary eds-btn--blunt-edge eds-btn--md']").click()
time.sleep(1)
#driver.find_element(By.LINK_TEXT,"Privacy Policy").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Policy").click()
driver.find_element(By.XPATH, "//input[@class='eds-text-field--password-field css-efet9v']").send_keys("embibe@20")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='eds-btn eds-btn--primary eds-btn--capsular eds-btn--sm eds-btn--block']").click()
time.sleep(5)
print(driver.current_url)

driver.close()