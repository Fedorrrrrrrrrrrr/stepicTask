from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test():
    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        button = browser.find_element(By.ID, "submit_button")
        button.click()

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

import math

def step_task():
    link = "http://suninjuly.github.io/get_attribute.html"

    try:

        browser = webdriver.Chrome()
        browser.get(link)

        treasure = browser.find_element(By.CSS_SELECTOR, "img[src='images/chest.png']")

        value_treasure = treasure.get_attribute("valuex")

        y = math.log(math.fabs(12*math.sin(float(value_treasure))))

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

