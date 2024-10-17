import requests
from datetime import datetime, timedelta    #To use pythons current date and time functionality, timedelta is used to use a future or past date and time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()

driver.find_element(By.ID, "datepicker2").click()
time.sleep(5)
current_date = datetime.now()
print(current_date)

next_day = current_date+timedelta(days=1)
print(next_day)
Next_day = (str(next_day.day))
print(Next_day)
current_month = datetime.now().month
current_year = datetime.now().year

next_month = (current_month % 12) + 1
next_month_year = f"{next_month}/{current_year}"
Month_Dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
select = Select(Month_Dropdown)
select.select_by_value(str(next_month_year))
Year_Dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the year']")
select = Select(Year_Dropdown)
select.select_by_visible_text("2024")
driver.find_element(By.LINK_TEXT, Next_day).click()
time.sleep(5) 