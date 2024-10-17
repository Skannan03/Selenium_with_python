import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()

actions = ActionChains(driver)
hover_element = driver.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
time.sleep(5)
actions.move_to_element(hover_element).perform()      #In order to perform the method perform command is used
driver.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()
time.sleep(5)