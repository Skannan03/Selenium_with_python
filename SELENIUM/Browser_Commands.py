from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get('https://opensource-demo.orangehrmlive.com/')
#driver.minimize_window()
driver.maximize_window()
#driver.fullscreen_window()
time.sleep(5)
forget_button = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header")
forget_button.click()
time.sleep(5)
driver.back();
time.sleep(5)
driver.forward();
time.sleep(5)
driver.refresh();
driver.close()