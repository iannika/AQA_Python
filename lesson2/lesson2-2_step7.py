from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    # имя файла, который будем загружать на сайт
    file_name = "file_example.txt"
    # собираем путь к файлу
    file_path = os.path.join(current_dir, file_name)          
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # отправляем файл
    element.send_keys(file_path)
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла



# путь автоматизатора.
# если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# # импортируем модуль
# import os
# # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
# current_dir = os.path.abspath(os.path.dirname(__file__))

# # имя файла, который будем загружать на сайт
# file_name = "file_example.txt"

# # получаем путь к file_example.txt
# file_path = os.path.join(current_dir, file_name)
# # отправляем файл
# element.send_keys(file_path)
# """




