from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="iphone"
driver.get(f"https://www.amazon.in/s?k={query}&crid=34OE191396ZSC&sprefix=iphone%2Caps%2C589&ref=nb_sb_noss_2")
elem = driver.find_element(By.CLASS_NAME, "s-widget-container")
print(elem.text)
time.sleep(6)
driver.close()