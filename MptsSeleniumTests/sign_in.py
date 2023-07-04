from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions as exceptions
import time


class SignInTest:

    def __init__(self, link):

        self.input_login = None

        self.input_password = None

        self.button_sign_in = None

        self.button_visibility_password = None

        try:
            self.browser = webdriver.Chrome()
            self.browser.get(link)

        except (exceptions.WebDriverException, exceptions.InvalidSelectorException) as e:
            print(e)
            self.browser.quit()

        # except:
        #     self.browser.quit()

    def good_test_sign_in(self, good_login, good_password):
        try:

            self.browser.refresh()
            self.refresh_elements()

            self.input_login.send_keys(good_login)

            self.input_password.send_keys(good_password)

            self.button_sign_in.click()

        except exceptions.ElementClickInterceptedException as e:
            print(e)
        # except:
        #     self.browser.quit()

    def bad_test_sign_in(self, bad_login, bad_password):
        try:
            self.browser.refresh()
            self.refresh_elements()
            self.input_login.send_keys(bad_login)
            self.input_password.send_keys(bad_password)
            self.button_sign_in.click()
        except exceptions.ElementClickInterceptedException as e:
            print(e)

    def button_visibility_password_test(self, test_password):
        try:
            self.browser.refresh()
            self.refresh_elements()
            self.input_password.send_keys(test_password)
            # input_password1 = self.browser.find_element(By.CSS_SELECTOR, "input[type='password']")

            print(self.input_password.text)
            self.button_visibility_password.click()
            self.refresh_elements()
            print(self.input_password.text)

            # if input_password1 == input_password2:
            #     print("Password visibility button works correctly")
            # else:
            #     print("Password visibility button not working correctly")
        except exceptions.ElementClickInterceptedException as e:
            print(e)

    def run_tests(self, good_login, good_password, bad_login, bad_password):
        try:
            test_password = "Test"

            self.button_visibility_password_test(test_password)
            self.bad_test_sign_in(bad_login, bad_password)
            self.good_test_sign_in(good_login, good_password)

        finally:
            time.sleep(40)
            self.browser.quit()

    def refresh_elements(self):

        try:

            self.input_login = self.browser.find_element(By.CSS_SELECTOR, "input[name='username']")

            self.input_password = self.browser.find_element(By.CSS_SELECTOR, "input[type='password']")

            self.button_sign_in = self.browser.find_element(By.CSS_SELECTOR, "button.q-btn")

            self.button_visibility_password = self.browser.find_element(By.CSS_SELECTOR,
                                                                        "i.q-icon[role = 'presentation']")
        except (exceptions.InvalidSelectorException, exceptions.NoSuchElementException) as e:
            print(e)
