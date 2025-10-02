from selenium.webdriver.common.by import By

class LoginPageLocators:
    BUTTON_USE_EMAIL = (By.XPATH, "//button[contains(text(), 'Use Email or Username')]")

    # input email
    EMAIL_INPUT = (By.NAME, "username")
    LOGIN_EMAIL_BUTTON = (By.XPATH, "//button[contains(text(), 'Log In')]")

    # input password
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(.,'Log In')]")


    # PASSWORD_INPUT = (By.ID, "password")
    # LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    # USER_INFO = (By.CSS_SELECTOR, ".user-info")