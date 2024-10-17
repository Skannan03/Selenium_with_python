#links that show not found or has some error

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

url = "https://jqueryui.com/"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)

all_links = driver.find_elements(By.TAG_NAME, 'a')  #anchor tags (a -href) in html code
print(f"Total no. of links on the page: {len(all_links)}")

for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken link: {href} (Status Code: {response.status_code})")
        #break

driver.quit()