import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = "https://stepik.org/lesson/236895/step/1"

answer = math.log(int(time.time()))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='ember33']")))
    button.click()
    input_login = browser.find_element(By.XPATH, "//input[@id='id_login_email']")
    input_login.send_keys("your_login")
    input_password = browser.find_element(By.XPATH, "//input[@id='id_login_password']")
    input_password.send_keys("your_password")
    button_sbm = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    button_sbm.click()  
    
    

    # input_text = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area")))
    input_text = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
    input_text.send_keys(str(answer))
        
        
    button_send = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button_send.click() 
    
    button_clear = browser.find_element(By.CSS_SELECTOR, 'button.again-btn')
    button_clear.click()
    
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__hint")))
    assert element == "Correct"
    browser.implicity_eait(20) 


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
    
    
    
    
    
    
    
    
    
    
