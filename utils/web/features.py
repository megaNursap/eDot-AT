from utils.common.config import Config
from utils.web.locator.login_page import LoginPageLocators
from utils.web.test_data import TestData
from utils.web.helper import wait_for_element, wait_for_clickable, wait_for_url_contains

class Features:

    @staticmethod
    def login(driver):
        driver.get(Config.BASE_URL)

        # klik tombol login pakai email
        use_email_button = wait_for_element(driver, LoginPageLocators.BUTTON_USE_EMAIL, timeout=30)
        use_email_button.click()

        # input email
        email_input = wait_for_element(driver, LoginPageLocators.EMAIL_INPUT, 10)
        email_input.send_keys(TestData.UserValid.VALID_EMAIL)

        login_button = wait_for_clickable(driver, LoginPageLocators.LOGIN_EMAIL_BUTTON, 10)
        login_button.click()

        # input password
        password_input = wait_for_element(driver, LoginPageLocators.PASSWORD_INPUT, 10)
        password_input.send_keys(TestData.UserValid.VALID_PASSWORD)

        login_submit_button = wait_for_clickable(driver, LoginPageLocators.LOGIN_SUBMIT_BUTTON, 10)
        login_submit_button.click()

        # verify success login
        wait_for_url_contains(driver, "https://esuite.edot.id/", 30)
        assert Config.BASE_URL in driver.current_url, "Login failed"
        print("Login successful")

        return driver
