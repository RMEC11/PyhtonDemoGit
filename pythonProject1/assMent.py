import time
from email import message

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

#serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
#driver = webdriver.Chrome(service=serv_chr)
#serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/geckodriver.exe")
#driver = webdriver.Firefox(service=serv_chr)

options = webdriver.FirefoxOptions("C:/Users/abhishek.tiwari_embi/Drivers/geckodriver.exe")
driver = webdriver.Firefox(executable_path=options)
#driver = webdriver.Firefox(options=options)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
activeWindow = driver.window_handles
driver.switch_to.window(activeWindow[1])
message = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
print(message)
var = message.split("at")[1].strip().split(" ")[0]
#userName = driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
#print(userName)
print(var)
driver.close()
driver.switch_to.window(activeWindow[0])
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(var)
driver.find_element(By.CSS_SELECTOR,"input[id='password']").send_keys("Testing")
driver.find_element(By.XPATH,"//input[@class='btn btn-info btn-md']").click()
time.sleep(2)
errMsg = driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text
print(errMsg)
driver.close()


