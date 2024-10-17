import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.selenium.dev/")
driver.switch_to.new_window()
driver.get("https://playwright.dev/")
number_of_tabs = len(driver.window_handles)
print(number_of_tabs)
tabs_value = driver.window_handles    #gives the value of the tab
print(tabs_value)
current_tab = driver.current_window_handle
print(current_tab)
driver.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()
first_tab = driver.window_handles[0]
if current_tab != first_tab:
    driver.switch_to.window(first_tab)  #if we do not use the swict to condition and run the below command it will show an error message

driver.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()