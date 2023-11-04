from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

  link = "http://suninjuly.github.io/get_attribute.html"

  browser = webdriver.Chrome()
  browser.get(link)
  
  x_element = browser.find_element(By.TAG_NAME , "img")
  x = x_element.get_attribute("valuex")
  y = calc(x)

  input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
  input_answer.send_keys(y)

  chek1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
  chek1.click()

  chek2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
  chek2.click()

  button = browser.find_element(By.CSS_SELECTOR, "[class = 'btn btn-default']")
  button.click()

finally:
    time.sleep(10)
    browser.quit()
