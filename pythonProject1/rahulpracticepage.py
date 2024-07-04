import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[class='form-control ng-untouched ng-pristine ng-invalid']").send_keys("Abhishek")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@class='form-control ng-untouched ng-pristine ng-invalid']").send_keys("abhi.rmec11@yahoo.co.in")
time.sleep(2)
driver.find_element(By.ID, 'exampleInputPassword1').send_keys("rmec11")
driver.find_element(By.CLASS_NAME, "form-check-input").click()
sel_gen = Select(driver.find_element(By.CSS_SELECTOR, "select[id='exampleFormControlSelect1']"))
sel_gen.select_by_visible_text("Female")
sel_gen.select_by_index(0)

driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio1']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio2']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio3']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio1']").click()
#driver.close()