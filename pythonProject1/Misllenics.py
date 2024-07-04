from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

serv_chr = Service("C:/Users/abhishek.tiwari_embi/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_chr, options=chrome_options)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.execute_script("window.scrollBy(0,500);")
driver.get_screenshot_as_file("1.png")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("Screen.png")