from utils.mobile.helper_mobile import *
from utils.mobile.locator.login_page import LoginLocators
from utils.mobile.locator.home_page import HomeLocators
from utils.mobile.test_data_mobile import TestDataMobile
from utils.mobile.features import logout_driver

def test_login_valid(logout_driver):
    driver = logout_driver
    
    # Company ID
    wait_and_send_keys(
        driver, 
        LoginLocators.COMPANY_ID_INPUT, 
        TestDataMobile.LoginValid.COMPANY_ID
    )

    # Username
    wait_and_send_keys(
        driver, 
        LoginLocators.USERNAME_INPUT, 
        TestDataMobile.LoginValid.COMPANY_EMAIL
    )

    # Password
    wait_and_send_keys(
        driver, 
        LoginLocators.PASSWORD_INPUT, 
        TestDataMobile.LoginValid.COMPANY_PASSWORD
    )

    # login button
    wait_and_click(driver, LoginLocators.LOGIN_BUTTON)

    # Assert Logo 
    logo = wait_for_element(driver, HomeLocators.LOGO)
    assert logo.is_displayed(), "Login failed: Logo not visible"

    # Assert Menu New Customer 
    new_customer = scroll_to_element(driver, HomeLocators.NEW_CUSTOMER)
    assert new_customer.is_displayed(), "Login failed: New Customer menu not visible"

    wait_and_click(driver, HomeLocators.MENU_DRAWER)

    # logout
    wait_and_click(driver, HomeLocators.LOGOUT)

    # Assert: back to login page
    login_field = wait_for_element(driver, LoginLocators.COMPANY_ID_INPUT, 20)
    assert login_field.is_displayed(), "Logout failed: Login page not displayed"
