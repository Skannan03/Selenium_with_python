from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()
images= browser.find_elements(By.TAG_NAME,value="img")
broken_images=[]
for i in images:
    src=i.get_attribute("src")
    if src:
        response= requests.get(src)
        if response.status_code !=200:
            broken_images.append(src)
            print(f"broken images found")
if broken_images:
    print("list of Broken images ")
    for i in broken_images:
        print(i)
else:
    print("no brokren images")