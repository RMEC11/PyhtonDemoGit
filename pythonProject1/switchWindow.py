import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_chr)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Click Here").click()
activeWindow = driver.window_handles
driver.switch_to.window(activeWindow[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
time.sleep(5)
driver.close()
driver.switch_to.window(activeWindow[0])
assert "Opening a new window" ==driver.find_element(By.TAG_NAME,"h3").text

