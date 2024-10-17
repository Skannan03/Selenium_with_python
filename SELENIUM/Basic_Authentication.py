import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth") #https://username:password@(link of the website)
driver.maximize_window()

username = "admin"
password = "admin"

time.sleep(5)