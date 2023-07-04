from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def step8_task(link):
    try:
        browser = webdriver.Chrome()

        browser.get(link)
        # Проверка только обязательных полей
        filling_required_fields(browser)

        # Проверка ввода всех полей
        browser.get(link)
        filling_all_fields(browser)

        # Проверка ввода без обязательных полей
        browser.get(link)
        filling_without_required_fields(browser)

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def filling_required_fields(browser):

    input_first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your first name']")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']")
    input_last_name.send_keys("Ivanov")
    input_email = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your email']")
    input_email.send_keys("test@mail.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


def filling_all_fields(browser):

    input_first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your first name']")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']")
    input_last_name.send_keys("Ivanov")
    input_email = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your email']")
    input_email.send_keys("test@mail.com")
    input_phone = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your phone:']")
    input_phone.send_keys("8987654321")
    input_address = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your address:']")
    input_address.send_keys("Moscow")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


def filling_without_required_fields(browser):

    input_phone = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your phone:']")
    input_phone.send_keys("8987654321")
    input_address = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your address:']")
    input_address.send_keys("Moscow")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
