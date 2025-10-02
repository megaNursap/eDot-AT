from selenium.webdriver.common.by import By

class SignPageLocators:
    SIGNATURE_VIEW = (By.ID, "id.edot.ework:id/signature_view")
    BTN_REGISTER = (By.XPATH, '//android.widget.Button[contains(@text,"Register")]')
    BTN_CONFIRM = (By.XPATH, '//android.widget.Button[contains(@text,"Yes")]')
