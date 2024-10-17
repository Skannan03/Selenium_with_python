import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
driver.maximize_window()

source_element = driver.find_element(By.ID, "column-a")
destination_element = driver.find_element(By.ID, "column-b")
actions = ActionChains(driver)
#actions.drag_and_drop(source_element,destination_element).perform()
actions.click_and_hold(source_element).move_to_element(destination_element).release().perform()
time.sleep(5)