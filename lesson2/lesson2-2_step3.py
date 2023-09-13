from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
    return int(num1) + int(num2)


link = "https://suninjuly.github.io/selects1.html"
# link = "https://suninjuly.github.io/selects2.html
browser = webdriver.Chrome()


try:
    
    browser.get(link)
    
    
    num1 = browser.find_element(By.ID, "num1")
    num1 = num1.text
    print(num1)
    num2 = browser.find_element(By.ID, "num2")
    num2 = num2.text
    print(num2)
    sum_num = int(num1) + int(num2)
    print(sum_num)

    # browser.find_element(By.TAG_NAME,"select").click()
    # browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    # Последняя строчка может выглядеть и так:
    # browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
    
    # упрощенный вариант
    
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(sum_num)) # ищем сумму
    
    btn = browser.find_element(By.CSS_SELECTOR,"button.btn")
    btn.click()
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла








