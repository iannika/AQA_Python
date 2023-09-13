from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    x_element = browser.find_element(By.ID,'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID,'answer')
    input1.send_keys(y)

    input2 = browser.find_element(By.ID,"robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID,"robotsRule")
    browser.execute_script("window.scrollBy(0, 100);")
    input3.click()
    input4 = browser.find_element(By.CSS_SELECTOR,"button.btn")
    input4.click()
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла








