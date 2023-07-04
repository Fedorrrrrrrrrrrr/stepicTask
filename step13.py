from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def step_task():
    link = "http://suninjuly.github.io/file_input.html"

    try:

        browser = webdriver.Chrome()
        browser.get(link)
        input_first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
        input_last_name.send_keys("Ivanov")
        input_email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
        input_email.send_keys("test@mail.com")

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.txt')
        print(path)
        #
        my_file = open(path, "w+")
        my_file.write("test")
        my_file.close()

        button_load_file = browser.find_element(By.CSS_SELECTOR, "#file")
        print(button_load_file.get_attribute("name"))
        button_load_file.send_keys(path)
        os.remove(path)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()
