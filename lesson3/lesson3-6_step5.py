import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()




class TestText ():
    
    @pytest.mark.parametrize("url", ["236895",
                                "236896",
                                "236897",
                                "236898",
                                "236899",
                                "236903",
                                "236904",
                                "236905"])
    
    
    def test_correct_text(self, browser, url):
        
        try:
        
            link = f"https://stepik.org/lesson/{url}/step/1"
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicity_eait(20) 
            
            
            button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='ember33']")))
            button.click()
            input_login = browser.find_element(By.XPATH, "//input[@id='id_login_email']")
            input_login.send_keys("your_login")
            input_password = browser.find_element(By.XPATH, "//input[@id='id_login_password']")
            input_password.send_keys("your_password")
            button_sbm = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
            button_sbm.click()  
            
            answer = math.log(int(time.time()))   
            
            input_text = browser.find_element(By.XPATH, ".ember-text-area")
            input_text.sens_keys(str(answer))
                
            button_send = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
            button_send.click()
            
            # element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__hint")))
            # print(element)
            
            # assert element == "Correct!", f"При значении {answer} тест упал с кодовым отвтом {element}"
                
            answer_code = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
            print(answer_code)
            assert answer_code=="Correct!",f'При значении {answer} тест упал с кодовым ответом {answer_code}'
        
        finally:
            time.sleep(5)
            browser.quit()
        
# if __name__ == "__main__":
#     pytest.__main__
#     print("Everything passed")
        
        # element = browser.find_element(By.CSS_SELECTOR,"p.smart-hints__hint")
        # clue = element.text
            
        # if clue != 'Correct!':
        #     with open('result.txt', 'a') as file:
        #         file.write(clue)
        
        
    
    
    
    
# пример https://github.com/eva-prus/stepik_auto_tests_course/blob/main/lesson3_6_ex4.py    
    
    
    
    
