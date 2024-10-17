from selenium import webdriver
from selenium.webdriver.common.by import By
import time

viewports = [(1500,679),(1207,225),(365,798),(414,896)]
driver = webdriver.Firefox()
driver.get("https://www.google.co.in/")
# driver.set_window_size(890,999)
# time.sleep(5)

try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(2)

finally:
    driver.close