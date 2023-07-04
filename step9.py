from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def step_task():
    link = "https://suninjuly.github.io/math.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
        x = x_element.text
        print(x)
        y = calc(x)
        print(y)

        test = browser.find_element(By.CSS_SELECTOR, "input#answer")
        test.send_keys(y)

        check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
        check_box.click()

        check_box1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
        check_box1.click()

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()


    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
