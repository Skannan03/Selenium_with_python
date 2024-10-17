from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()

dropdown_element = driver.find_element(By.ID, "dropdown")
# select = Select(dropdown_element)  #3 ways to select an option
# option_count = len(select.options)
# 1. Select the value by visible text
# 2. Select the value by index
# 3. Select the option by using value

#select.select_by_visible_text("Option 2")
#select.select_by_index(2)
#select.select_by_value("1")

# expected_count = 3
# if(option_count == expected_count):
#     print("Testcase Passed. Count is Correct")
# else:
#     print("Testcase Failed. Count is Incorrect")

target_value = "Option 2"
select = Select(dropdown_element)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"Option '{target_value}' not found")


# Covered Topics:
# How to interact with dropdown 
# How to use Select class
# 3 different methods
# Count dropdown values
# Loop dropdown values and if desired value is found select the value