from selenium.webdriver.common.by import By

class LoginLocators:
    COMPANY_ID_INPUT = (By.ID, "id.edot.ework:id/tv_company_id")
    USERNAME_INPUT   = (By.ID, "id.edot.ework:id/tv_username")
    PASSWORD_INPUT   = (By.ID, "id.edot.ework:id/tv_password")
    LOGIN_BUTTON     = (By.ID, "id.edot.ework:id/button_text")
