from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ivonav")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("ivan@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    # имя файла, который будем загружать на сайт
    file_name = "file_example.txt"
    # собираем путь к файлу
    file_path = os.path.join(current_dir, file_name)          
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # отправляем файл
    element.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла

