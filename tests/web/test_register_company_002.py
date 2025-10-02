import time
from utils.common.config import Config
from utils.web.locator.register_company import RegisterCompanyLocators
from utils.web.locator.manage_company import ManageCompanyLocators, CompaniesProfileAccLocators
from utils.web.test_data import TestData
from utils.web.helper import (
    wait_for_element,
    wait_for_clickable,
    wait_for_url_contains,
    wait_for_input_file,
    get_test_file_path,
)
from utils.web.features import Features

class TestRegisterCompany:

    def test_register_company(self, login, company_name):
        # Pre-condition:
        driver = login 

        # Page 1 - Register Company
        # Navigate to Companies page
        companies_link = wait_for_clickable(driver, RegisterCompanyLocators.COMPANIES_LINK, 30)
        companies_link.click()
        wait_for_url_contains(driver, "/companies", 20)

        # Add Company
        add_button = wait_for_clickable(driver, RegisterCompanyLocators.ADD_COMPANY_BUTTON, 10)
        add_button.click()
        wait_for_url_contains(driver, "/companies/registration-companies", 10)

        # Company Name
        wait_for_element(driver, RegisterCompanyLocators.COMPANY_NAME_INPUT).send_keys(company_name)
        # Email
        wait_for_element(driver, RegisterCompanyLocators.EMAIL_INPUT).send_keys(TestData.CompanyProfileValid.COMPANY_EMAIL)

        # Phone
        wait_for_element(driver, RegisterCompanyLocators.PHONE_INPUT).send_keys(TestData.CompanyProfileValid.COMPANY_PHONE)

        # Industry Type
        wait_for_clickable(driver, RegisterCompanyLocators.INDUSTRY_TYPE_DROPDOWN).click()
        wait_for_clickable(driver, RegisterCompanyLocators.INDUSTRY_TYPE_RETAIL).click()

        # Company Type
        wait_for_clickable(driver, RegisterCompanyLocators.COMPANY_TYPE_DROPDOWN).click()
        wait_for_clickable(driver, RegisterCompanyLocators.COMPANY_TYPE_IMPORT_EXPORT).click()

        # Language
        wait_for_clickable(driver, RegisterCompanyLocators.LANGUAGE_DROPDOWN).click()
        wait_for_clickable(driver, RegisterCompanyLocators.LANGUAGE_ENGLISH).click()

        # Address → random street
        wait_for_element(driver, RegisterCompanyLocators.ADDRESS_INPUT).send_keys(TestData.CompanyProfileValid.COMPANY_ADDRESS)

        # Country
        wait_for_clickable(driver, RegisterCompanyLocators.COUNTRY_DROPDOWN).click()
        wait_for_clickable(driver, RegisterCompanyLocators.COUNTRY_INDONESIA).click()

        # Province
        wait_for_clickable(driver, RegisterCompanyLocators.PROVINCE_DROPDOWN).click()
        province_search = wait_for_element(driver, RegisterCompanyLocators.PROVINCE_SEARCH_INPUT)
        province_search.send_keys(TestData.CompanyProfileValid.PROVINCE)
        wait_for_clickable(driver, RegisterCompanyLocators.PROVINCE_JAWA_TIMUR).click()

        # City
        wait_for_clickable(driver, RegisterCompanyLocators.CITY_DROPDOWN).click()
        city_search = wait_for_element(driver, RegisterCompanyLocators.CITY_SEARCH_INPUT)
        city_search.send_keys(TestData.CompanyProfileValid.CITY)
        wait_for_clickable(driver, RegisterCompanyLocators.CITY_KOTA_MALANG).click()

        # District
        wait_for_clickable(driver, RegisterCompanyLocators.DISTRICT_DROPDOWN).click()
        district_search = wait_for_element(driver, RegisterCompanyLocators.DISTRICT_SEARCH_INPUT)
        district_search.send_keys(TestData.CompanyProfileValid.DISTRICT)
        wait_for_clickable(driver, RegisterCompanyLocators.DISTRICT_KEDUNGKANDANG).click()

        # Sub-District
        wait_for_clickable(driver, RegisterCompanyLocators.SUB_DISTRICT_DROPDOWN).click()
        sub_district_search = wait_for_element(driver, RegisterCompanyLocators.SUB_DISTRICT_SEARCH_INPUT)
        sub_district_search.send_keys(TestData.CompanyProfileValid.SUB_DISTRICT)
        wait_for_clickable(driver, RegisterCompanyLocators.SUB_DISTRICT_SAWOJAJAR).click()

        # Next / Submit
        submit_button = wait_for_clickable(driver, RegisterCompanyLocators.NEXT_BUTTON, 10)
        submit_button.click()

        # Page 2 - Register Legal
        # Add Document
        wait_for_clickable(driver, RegisterCompanyLocators.ADD_DOCUMENT_BUTTON).click()

        # Choose Legal Document
        wait_for_clickable(driver, RegisterCompanyLocators.LEGAL_DOCUMENT_DROPDOWN).click()

        # input search
        search_input = wait_for_element(driver, RegisterCompanyLocators.LEGAL_DOCUMENT_SEARCH_INPUT)
        search_input.send_keys("Identification Card")
        wait_for_clickable(driver, RegisterCompanyLocators.LEGAL_DOCUMENT_IDENTIFICATION_CARD).click()

        # upload file
        file_path = get_test_file_path("arsenal.jpg")
        upload_file_input = wait_for_input_file(driver, RegisterCompanyLocators.UPLOAD_FILE_INPUT)
        upload_file_input.send_keys(file_path)

        # klik submit document
        submit_doc = wait_for_clickable(driver, RegisterCompanyLocators.SUBMIT_DOCUMENT_BUTTON, 20)
        submit_doc.click()

        # next after upload doc
        next_after_upload = wait_for_clickable(driver, RegisterCompanyLocators.NEXT_BUTTON_AFTER_UPLOAD_DOC, 20)
        next_after_upload.click()

        # Page 3 - Create Your Branch
        # input branch name
        branch_input = wait_for_element(driver, RegisterCompanyLocators.BRANCH_NAME_INPUT, 10)
        branch_input.clear()
        branch_input.send_keys("Headquarter")

        # fill in company data
        fill_button = wait_for_clickable(driver, RegisterCompanyLocators.AUTO_FILL_COMPANY_DATA_BUTTON, 10)
        fill_button.click()

        # select all
        checkbox_terms_condition = wait_for_clickable(driver, RegisterCompanyLocators.CHECKBOX_POLICY_TERM_CONDITION)
        checkbox_terms_condition.click()

        # register
        register_btn = wait_for_clickable(driver, RegisterCompanyLocators.REGISTER_BUTTON, 10)
        register_btn.click()

        # ------------------------------------------------------------------------
        # Verify company registered successfully
        # Navigate to Companies page
        companies_link = wait_for_clickable(driver, RegisterCompanyLocators.COMPANIES_LINK, 30)
        companies_link.click()
        wait_for_url_contains(driver, "/companies", 20)

        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        
        # Find manage under company name that was created
        created_company = wait_for_clickable(driver, ManageCompanyLocators.manage_button_locator(company_name), 20)
        created_company.click()

        time.sleep(2)
        driver.refresh()
        time.sleep(2)

        # Validate Company Name
        company_name_input = wait_for_element(driver, CompaniesProfileAccLocators.COMPANY_NAME_INPUT, 10)
        actual_value = company_name_input.get_attribute("value")
        assert actual_value == company_name

        # Validate Industry Type
        # Cari element industry type
        industry_type = wait_for_element(driver, CompaniesProfileAccLocators.INDUSTRY_TYPE, 10)
        actual_industry = industry_type.text
        assert actual_industry == TestData.CompanyProfileValid.INDUSTRY_TYPE

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

        