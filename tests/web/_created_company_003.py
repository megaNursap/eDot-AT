import time
from utils.common.config import Config
from utils.web.locator.register_company import RegisterCompanyLocators
from utils.web.locator.manage_company import ManageCompanyLocators, CompaniesProfileAccLocators
from utils.web.test_data import TestData
from utils.web.helper import wait_for_element, wait_for_clickable, wait_for_url_contains
from utils.web.features import Features

class TestCreatedCompany:

    def test_created_company(self, login, company_name):
        # Pre-condition:
        driver = login 

        # Navigate to Companies page
        companies_link = wait_for_clickable(driver, RegisterCompanyLocators.COMPANIES_LINK, 30)
        companies_link.click()
        wait_for_url_contains(driver, "/companies", 20)

        time.sleep(3)
        
        # Find manage under company name that was created
        created_company = wait_for_clickable(driver, ManageCompanyLocators.manage_button_locator(company_name), 20)
        created_company.click()

        # Validate Company Name
        company_name_input = wait_for_element(driver, CompaniesProfileAccLocators.COMPANY_NAME_INPUT, 10)
        actual_value = company_name_input.get_attribute("value")
        assert actual_value == TestData.CompanyProfileValid.COMPANY_NAME

        # Validate Industry Type
        # Cari element industry type
        industry_type = wait_for_element(driver, CompaniesProfileAccLocators.INDUSTRY_TYPE, 10)
        actual_industry = industry_type.text
        assert actual_industry == TestData.CompanyProfileValid.INDUSTRY_TYPE

        # Input fields
        company_name = wait_for_element(driver, CompaniesProfileAccLocators.COMPANY_NAME_INPUT)
        assert company_name.get_attribute("value") == TestData.CompanyProfileValid.COMPANY_NAME

        email = wait_for_element(driver, CompaniesProfileAccLocators.EMAIL_INPUT)
        assert email.get_attribute("value") == TestData.CompanyProfileValid.COMPANY_EMAIL

        phone = wait_for_element(driver, CompaniesProfileAccLocators.PHONE_INPUT)
        assert phone.get_attribute("value") == TestData.CompanyProfileValid.COMPANY_PHONE

        address = wait_for_element(driver, CompaniesProfileAccLocators.ADDRESS_TEXTAREA)
        assert address.get_attribute("value") == TestData.CompanyProfileValid.COMPANY_ADDRESS

        # Dropdowns
        industry = wait_for_element(driver, CompaniesProfileAccLocators.INDUSTRY_TYPE)
        assert industry.text == TestData.CompanyProfileValid.INDUSTRY_TYPE

        business_type = wait_for_element(driver, CompaniesProfileAccLocators.BUSINESS_TYPE)
        assert business_type.text == TestData.CompanyProfileValid.COMPANY_TYPE

        country = wait_for_element(driver, CompaniesProfileAccLocators.COUNTRY)
        assert country.text == TestData.CompanyProfileValid.COUNTRY

        province = wait_for_element(driver, CompaniesProfileAccLocators.PROVINCE)
        assert province.text == TestData.CompanyProfileValid.PROVINCE

        city = wait_for_element(driver, CompaniesProfileAccLocators.CITY)
        assert city.text == TestData.CompanyProfileValid.CITY

        district = wait_for_element(driver, CompaniesProfileAccLocators.DISTRICT)
        assert district.text == TestData.CompanyProfileValid.DISTRICT

        zone = wait_for_element(driver, CompaniesProfileAccLocators.ZONE)
        assert zone.text == TestData.CompanyProfileValid.SUB_DISTRICT
        

    

