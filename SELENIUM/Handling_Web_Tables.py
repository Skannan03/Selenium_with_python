import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,700)")
table = driver.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")
rows_count = len(rows)
print(rows_count)
target_value = "Australia"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Found value '{target_value}'")
            found = True
            break
    if found:
        break
if not found:
    print(f"Target Value '{target_value}' not Found")