import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\agath\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://betfred.com/")
print(driver.title)
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
time.sleep(1230)
assert "No results found." not in driver.page_source
driver.close()