from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
    
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"


    # assert people_checked == "true", "People radio is not selected by default"
    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None
    
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла








