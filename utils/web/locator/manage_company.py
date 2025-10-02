from selenium.webdriver.common.by import By

class ManageCompanyLocators:
    @staticmethod
    def manage_button_locator(companyName):
        return (By.XPATH, f"//div[contains(@class,'text-lg') and text()='{companyName}']"
                        "/ancestor::div[contains(@class,'rounded-lg')]//button[text()='Manage']")


class CompaniesProfileAccLocators:
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Input Company Name']")
    INDUSTRY_TYPE = (By.XPATH, "//button[@role='combobox']//span")
    BUSINESS_TYPE = (By.XPATH, "(//button[@role='combobox']//span[@class='text-gray-700'])[2]")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Input Email']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='Input Mobile Number']")
    ADDRESS_TEXTAREA = (By.XPATH, "//textarea[@placeholder='Input Company Address']")
    COUNTRY = (By.XPATH, "//span[contains(text(),'Country')]/following::button[1]/span")
    PROVINCE = (By.XPATH, "//span[contains(text(),'Country')]/following::button[2]/span")
    CITY = (By.XPATH, "//span[contains(text(),'Country')]/following::button[3]/span")
    DISTRICT = (By.XPATH, "//span[contains(text(),'Country')]/following::button[4]/span")
    ZONE = (By.XPATH, "//span[contains(text(),'Country')]/following::button[5]/span")