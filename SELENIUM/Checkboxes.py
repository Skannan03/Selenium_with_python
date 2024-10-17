from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click() #for checking a single box
time.sleep(5)
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']") #used to identify all the checkboxes in the url
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)  # checks all the checkboxes

checked_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1

expected_count = 7
if checked_count == expected_count:
    print('Checkbox count verified')
else:
    print('Checkbox count mismatch')
time.sleep(5)
driver.close()