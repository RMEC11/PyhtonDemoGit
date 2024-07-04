import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_chr)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()
products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    productname = product.find_element(By.XPATH,"div/h4/a").text
    if productname == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='country']").send_keys("ind")
wait= WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
#time.sleep(5)
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
finaltext= driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(finaltext)
assert "Success! Thank you! " in finaltext
driver.close()


