from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://www.guru99.com/live-selenium-project.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input = browser.find_element(By.ID, "awf_field-93653884")
    input.send_keys("iva89@gmail.com")
    button = browser.find_element(By.ID, "af-submit-image-482158182")
    button.click()

    
finally:
    time.sleep(5)
    browser.quit()