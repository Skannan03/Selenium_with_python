import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()

#Switching to TOP Frame
driver.switch_to.frame("frame-top")

#Switching to TOP Frame
driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID, "content").text
print("Content in middle frame", content)

#Switch to Default Content

driver.switch_to.default_content()

#Switching to BOTTOM Frame
driver.switch_to.frame("frame-bottom")

content_bottom = driver.find_element(By.TAG_NAME, "body").text
print("Content in bottom frame", content_bottom)