import time

from selenium import webdriver
# chrome_path = 'C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe'
#driver = webdriver.Chrome(executable_path=chrome_path)
from selenium.webdriver.chrome.service import Service

serv_obj= Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#driver= webdriver.Firefox() # Need to downlaod firefox driver and mention the path
url= "https://www.embibe.com/"
driver.get(url)
driver.maximize_window()
print(driver.title)
if url==(driver.current_url):
    print("Success:- "+ driver.current_url)
else:
    print("Invalid Url")



time.sleep(2)
driver.close()
