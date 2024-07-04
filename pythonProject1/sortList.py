from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("headless")

browsersortlist1 = []
serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_chr,options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='#/offers']").click()
chromehandel= driver.window_handles
driver.switch_to.window(chromehandel[1])
driver.find_element(By.XPATH,"//option[@value='10']").click()
#driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
browsersortlist = driver.find_elements(By.XPATH,"//tr/td[1]")

for ele in browsersortlist:
    browsersortlist1.append(ele.text)
print(browsersortlist1)

sortchecklist = browsersortlist1.copy()
browsersortlist1.sort()

assert browsersortlist1 == sortchecklist


