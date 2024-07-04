from selenium import webdriver


#geckodriver_path = "C:/Users/abhishek.tiwari_embi/Drivers/geckodriver.exe"

#serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
#driver = webdriver.Chrome(service=serv_chr)
from selenium.webdriver.firefox.service import Service

serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/geckodriver.exe")
driver = webdriver.Firefox(service=serv_chr)

#options = webdriver.FirefoxOptions("C:/Users/abhishek.tiwari_embi/Drivers/geckodriver.exe")
#driver = webdriver.Firefox(executable_path='C:/Users/abhishek.tiwari_embi/Drivers/geckodriver.exe')