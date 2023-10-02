from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest


class PythonOrgSearch(unittest.TestCase):
   def setUp(self):
      self.driver = webdriver.Chrome()
      
   def test1(self):
      driver = self.driver
      driver.get("http://suninjuly.github.io/registration1.html")

      input1 = driver.find_element(By.CSS_SELECTOR, ".first_block .first_class input")    #'.first[required]'
      input1.send_keys("Ivan")
      input2 = driver.find_element(By.CSS_SELECTOR, ".first_block .second_class input")    #'.second[required]'
      input2.send_keys("Ivanov")
      input3 = driver.find_element(By.CSS_SELECTOR, ".first_block .third_class input")    #'.third[required]'
      input3.send_keys("ivan@gmail.com")
      
      button = driver.find_element(By.CSS_SELECTOR, "button.btn")
      button.click()   
      
   def test2(self):
      driver = self.driver
      driver.get("http://suninjuly.github.io/registration2.html")

      input1 = driver.find_element(By.CSS_SELECTOR, ".first_block .first_class input")    #'.first[required]'
      input1.send_keys("Ivan")
      input2 = driver.find_element(By.CSS_SELECTOR, ".first_block .second_class input")    #'.second[required]'
      input2.send_keys("Ivanov")
      input3 = driver.find_element(By.CSS_SELECTOR, ".first_block .third_class input")    #'.third[required]'
      input3.send_keys("ivan@gmail.com")
      
      button = driver.find_element(By.CSS_SELECTOR, "button.btn")
      button.click()
      self.assertNotIn("No resul found.", driver.page_source)
      
   def tearDown(self):
      self.driver.close()
      
      
if __name__ == "__main__":
   unittest.main()         




# example
# https://ucarecdn.com/736a013d-17df-4bc2-bd64-b6e1511ab697/
# https://selenium-python.readthedocs.io/getting-started.html#using-selenium-to-write-tests
   
   