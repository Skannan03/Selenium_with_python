import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://demo.automationtesting.in/Resizable.html")
driver.maximize_window()

resizable_element = driver.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
Initial_element_size = driver.find_element(By.XPATH, "//div[@id='resizable']")
initial_size = Initial_element_size.size
print("Initial Size:", initial_size)
time.sleep(5)
action_chains =ActionChains(driver)
action_chains.click_and_hold(resizable_element).move_by_offset(100,200).release().perform()
time.sleep(5)
resized_element = Initial_element_size.size
print("Resized Element:", resized_element)
