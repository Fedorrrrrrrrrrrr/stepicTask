from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def step_task():
    try:
        browser = webdriver.Chrome()

        browser.get("http://suninjuly.github.io/explicit_wait2.html")
        button = browser.find_element(By.CSS_SELECTOR, "#book")
        WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))

        button.click()
        number = browser.find_element(By.CSS_SELECTOR, "#input_value")
        print(number.text)
        input = browser.find_element(By.CSS_SELECTOR, "#answer")
        input.send_keys(cal_math(int(number.text)))
        print(1)
        # browser.execute_script("button = document.querySelector('button#solve')[0];button.scrollIntoView(true);")
        button1 = browser.find_element(By.CSS_SELECTOR, "button#solve")
        print(2)
        button1.click()
        print(3)
    finally:
        time.sleep(70)
        browser.quit()


def cal_math(value):
    return math.log(math.fabs(12 * math.sin(float(value))))
