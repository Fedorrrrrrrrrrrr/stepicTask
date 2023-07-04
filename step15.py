from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def step_task():
    link = "http://suninjuly.github.io/redirect_accept.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
        button.click()
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        # alert = browser.switch_to.alert
        # alert.accept()
        #
        number = browser.find_element(By.CSS_SELECTOR, "#input_value")
        print(number.text)
        input = browser.find_element(By.CSS_SELECTOR, "#answer")
        input.send_keys(cal_math(int(number.text)))

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()



    finally:
        time.sleep(70)
        browser.quit()
        
def cal_math(value):
    return math.log(math.fabs(12 * math.sin(float(value))))
