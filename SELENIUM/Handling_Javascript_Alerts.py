import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#JS Alerts
# Alert_Button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
# Alert_Button.click()

# #There will be locator for the alert message box
# alert = driver.switch_to.alert
# alert_text = alert.text
# print(alert_text)

# time.sleep(5)
# alert.accept()
# time.sleep(5)


#############################################################################################################
# #JS Confirm
# Alert_Button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
# Alert_Button.click()

# #There will be locator for the alert message box
# alert = driver.switch_to.alert
# alert_text = alert.text
# print(alert_text)

# time.sleep(5)
# alert.dismiss() #cancel button is clicked
# time.sleep(5)
#############################################################################################

#JS Prompt
Alert_Button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
Alert_Button.click()

#There will be locator for the alert message box
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

time.sleep(5)
alert.send_keys("This is Selenium with python")
alert.accept() 
time.sleep(5)