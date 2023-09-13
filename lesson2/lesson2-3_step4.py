from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.ID,"answer")
    input.send_keys(y)
    
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()


