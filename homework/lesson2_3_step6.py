from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element(By.CSS_SELECTOR, "[class = 'trollface btn btn-primary']")
    button_1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)

    button_2 = browser.find_element(By.CSS_SELECTOR, "[class = 'btn btn-primary']")
    button_2.click()

finally:
   time.sleep(10)
   browser.quit()

    