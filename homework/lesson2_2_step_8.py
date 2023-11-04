from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('Evgeniya')

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('Www')

    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('test@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    but_file = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    but_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "[class = 'btn btn-primary']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
