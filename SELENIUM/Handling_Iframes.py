import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

Text_Editor = driver.find_elements(By.ID, "tinymce")
Text_Editor.clear()
Text_Editor.send_keys("This is Selenium")
time.sleep(5)

driver.switch_to.default_content()   #Required to run the below command as for upper commands driver has switced to iframes section
Selenium_link = driver.find_element(By.XPATH, "//a[normalize-space()='Elemental Selenium']")
Selenium_link.click()