import pytest
from selenium.common.exceptions import TimeoutException
from utils.mobile.locator.login_page import LoginLocators
from utils.mobile.locator.home_page import HomeLocators
from utils.mobile.test_data_mobile import TestDataMobile
from utils.mobile.helper_mobile import *

@pytest.fixture(scope="function")
def login_driver(driver):
    try:
        # Check if already logged in by looking for an element on the home page
        wait_for_element(driver, HomeLocators.LOGO, timeout=5)
    except TimeoutException:
        # Not logged in, perform login
        wait_and_send_keys(driver, LoginLocators.COMPANY_ID_INPUT, TestDataMobile.LoginValid.COMPANY_ID)
        wait_and_send_keys(driver, LoginLocators.USERNAME_INPUT, TestDataMobile.LoginValid.COMPANY_EMAIL)
        wait_and_send_keys(driver, LoginLocators.PASSWORD_INPUT, TestDataMobile.LoginValid.COMPANY_PASSWORD)
        wait_and_click(driver, LoginLocators.LOGIN_BUTTON)

        # Verify login was successful
        logo = wait_for_element(driver, HomeLocators.LOGO, timeout=15)
        assert logo.is_displayed(), "Login failed"

    yield driver

@pytest.fixture(scope="function")
def logout_driver(driver):
    try:
        logo = wait_for_element(driver, HomeLocators.LOGO, timeout=5)
        if logo.is_displayed():
            wait_and_click(driver, HomeLocators.MENU_DRAWER)
            wait_and_click(driver, HomeLocators.LOGOUT)
    except TimeoutException:
        pass

    yield driver