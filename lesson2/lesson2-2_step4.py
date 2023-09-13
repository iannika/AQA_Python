from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

    
link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
    
try:
    
    browser.get(link)
    browser.execute_script("alert('Robots at work');")
    browser.quit()
    
    
    # Обратите внимание, что исполняемый JavaScript нужно заключать в 
    # кавычки (двойные или одинарные). Если внутри скрипта вам также 
    # понадобится использовать кавычки, а для выделения скрипта вы уже 
    # используете двойные кавычки, то в скрипте следует поставить 
    # одинарные:

    browser.execute_script("document.title='Script executing';")
    # Такой формат записи тоже будет работать:

    browser.execute_script('document.title="Script executing";')
    # Можно с помощью этого метода выполнить сразу несколько инструкций, 
    # перечислив их через точку с запятой. Изменим сначала заголовок 
    # страницы, а затем вызовем alert:

    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    
    alert = browser.switch_to.alert
    alert.accept()
        
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла

