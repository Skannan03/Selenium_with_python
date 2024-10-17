from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://www.selenium.dev/")
browser.switch_to.new_window()
browser.get("https://playwright.dev/")
num = len(browser.window_handles)
print(num)
tabs_val = browser.window_handles
print(tabs_val)
currnt_tab=browser.current_window_handle
print(currnt_tab)
browser.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()

first_tab =browser.window_handles[0]
if currnt_tab != first_tab:
    browser.switch_to.window(first_tab)
browser.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()