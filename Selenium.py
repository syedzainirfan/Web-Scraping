from selenium import webdriver # open and control Browser
from selenium.webdriver.common.keys import Keys # Keyboard ki keys ke liye like enter ,return shift etc.
from selenium.webdriver.common.by import By # Finds elements on webpage
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(6)
driver.close()
