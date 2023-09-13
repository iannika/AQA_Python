from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # browser.execute_script("window.scrollBy(0, 100);")
    button.click()
    
    
    
        
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла

