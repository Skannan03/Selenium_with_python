import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from openpyxl import load_workbook


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

 
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")   
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()

driver.quit()