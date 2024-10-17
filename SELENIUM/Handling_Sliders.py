import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/horizontal_slider")
driver.maximize_window()

slider = driver.find_element(By.XPATH, "//input[@type='range']")
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(25,0).release().perform()       #xaxis,yaxis for move_by_offset
time.sleep(5)