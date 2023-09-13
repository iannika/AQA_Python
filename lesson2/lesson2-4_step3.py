from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/wait1.html"
browser.get(link)


try:
    time.sleep(3)
    button = browser.find_element(By.ID, "verify")
    button.click()
    time.sleep(1)
    message = browser.find_element(By.ID, "verify_message")
    
    assert "seccessful" in message.text
    
    
finally:
    time.sleep(5)
    browser.quit()


