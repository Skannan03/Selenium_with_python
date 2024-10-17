import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")   
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
element.click()
driver.quit()