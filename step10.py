from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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

