import requests
from datetime import datetime, timedelta    #To use pythons current date and time functionality, timedelta is used to use a future or past date and time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://globalsqa.com/demo-site/datepicker/")
driver.maximize_window()
driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()
frameLo = driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(frameLo)
time.sleep(5)

#Simple Date Picker
driver.find_element(By.CSS_SELECTOR, "#datepicker").click()

current_date = datetime.now()
next_date = current_date+timedelta(days=1) #current date + 1

formatted_date = next_date.strftime("%m/%d/%y")
driver.find_element(By.CSS_SELECTOR, "#datepicker").send_keys(formatted_date + Keys.TAB)  #Keys.TAB clicks the tab key
time.sleep(5)
driver.quit()