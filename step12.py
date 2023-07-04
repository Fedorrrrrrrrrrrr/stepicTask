from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def step_task():
    link = "https://SunInJuly.github.io/execute_script.html"

    try:

        browser = webdriver.Chrome()
        browser.get(link)

        treasure = browser.find_element(By.CSS_SELECTOR, "span#input_value")

        value_treasure = treasure.text

        y = math.log(math.fabs(12*math.sin(float(value_treasure))))
        print(y)
        test = browser.find_element(By.CSS_SELECTOR, "input#answer")
        test.send_keys(y)
        print(1)

        check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
        check_box.click()
        print(2)
        browser.execute_script("input = document.querySelector('span#input_value');input.scrollIntoView(true);")

        check_box1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
        check_box1.click()
        print(3)
        browser.execute_script("button = document.getElementsByTagName('button')[0];button.scrollIntoView(true);")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()





    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

