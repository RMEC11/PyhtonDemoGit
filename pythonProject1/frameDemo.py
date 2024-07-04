import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_chr)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='/frames']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[href='/iframe']").click()
driver.switch_to.frame("mce_0_ifr")
#alert = driver.switch_to.alert
#alert.dismiss()
#driver.find_element(By.XPATH,"//div[@class='tox-icon']").click()
#driver.find_element(By.ID,"tinymce").clear()
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
driver.close()
