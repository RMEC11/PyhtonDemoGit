import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_chr)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("me")
time.sleep(2)
actualList=["Musk Melon - 1 Kg", "Pomegranate - 1 Kg", "Water Melon - 1 Kg"]
expetedList=[]
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count=len(results)
assert count > 0

for result in results:
    expetedList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()
print(expetedList)
#assert expetedList == actualList
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
total = 0
for price in prices:
    total = total + int(price.text)
print(total)

totalAmount = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
assert total == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(5)
discAmount= float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(discAmount)
assert  totalAmount > discAmount
#wait = WebDriverWait(driver, 10)
#wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "promoInfo")))
codeText = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(codeText)
campText ='Code applied ..!'
assert campText == codeText
driver.close()
