from selenium.webdriver.common.by import By

class RegisterCompanyLocators:
    # Page 1
    # Navigation
    COMPANIES_LINK = (By.LINK_TEXT, "Companies")
    ADD_COMPANY_BUTTON = (By.XPATH, "//button[contains(., '+ Add Company')]")
    # Company Details
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Input Company Name']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Input Email']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='Input Phone']")
    # Industry Type
    INDUSTRY_TYPE_DROPDOWN = (By.XPATH, "//button[span[text()='Choose Industry Type']]")
    INDUSTRY_TYPE_RETAIL = (By.XPATH, "//div[span[text()='Retail']]")
    # Company Type
    COMPANY_TYPE_DROPDOWN = (By.XPATH, "//button[span[text()='Choose Company Type']]")
    COMPANY_TYPE_IMPORT_EXPORT = (By.XPATH, "//div[span[text()='Importer/Exporter']]")
    # Language
    LANGUAGE_DROPDOWN = (By.XPATH, "//button[span[text()='Choose Language']]")
    LANGUAGE_ENGLISH = (By.XPATH, "//div[span[text()='English']]")
    # Address
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='Input Address']")
    # Country
    COUNTRY_DROPDOWN = (By.XPATH, "//button[span[text()='Choose Country']]")
    COUNTRY_INDONESIA = (By.XPATH, "//div[span[text()='Indonesia']]")
    # Province
    PROVINCE_DROPDOWN = (By.XPATH, "//button[span[text()='Choose Province']]")
    PROVINCE_JAWA_TIMUR = (By.XPATH, "//div[@role='option' and text()='JAWA TIMUR']")
    PROVINCE_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")
    # City
    CITY_DROPDOWN = (By.XPATH, "//button[span[text()='Choose City']]")
    CITY_KOTA_MALANG = (By.XPATH, "//div[@role='option' and text()='KOTA MALANG']")
    CITY_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")
    # District
    DISTRICT_DROPDOWN = (By.XPATH, "//button[span[text()='Choose District']]")
    DISTRICT_KEDUNGKANDANG = (By.XPATH, "//div[@role='option' and text()='KEDUNGKANDANG']")
    DISTRICT_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")
    # Sub-District
    SUB_DISTRICT_DROPDOWN = (By.XPATH, "//button[span[text()='Choose Sub District']]")
    SUB_DISTRICT_SAWOJAJAR = (By.XPATH, "//div[@role='option' and text()='SAWOJAJAR']")
    SUB_DISTRICT_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")
    # Next / Submit
    NEXT_BUTTON = (By.XPATH, "//div[@class='mt-5 flex justify-end']//button[contains(., 'Next')]")

    # Page 2
    ADD_DOCUMENT_BUTTON = (By.XPATH, "//button[contains(text(), '+ Add Document')]")
    LEGAL_DOCUMENT_DROPDOWN = (By.XPATH, "//button[.//span[text()='Choose Legal Document']]")
    LEGAL_DOCUMENT_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search data...']")
    LEGAL_DOCUMENT_IDENTIFICATION_CARD = (By.XPATH, "//div[@role='option' and text()='Identification Card']")
    UPLOAD_FILE_INPUT = (By.XPATH, "//label[.//span[text()='Upload File Document']]//input[@type='file']")
    SUBMIT_DOCUMENT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit Document')]")
    NEXT_BUTTON_AFTER_UPLOAD_DOC = (By.XPATH, "//button[normalize-space(text())='Next']")

    # Page 3
    BRANCH_NAME_INPUT = (By.XPATH, "//input[@placeholder='Input Branch Name']")
    AUTO_FILL_COMPANY_DATA_BUTTON = (By.XPATH, "//button[contains(text(), 'Fill in with the same data from the Company records')]")
    CHECKBOX_POLICY_TERM_CONDITION = (By.ID, "select-all")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Register')]")


