import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.web.features import Features
from utils.web.test_data import TestData


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,800")
    # options.add_argument("--headless=new")  # aktifkan for CI/CD
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    # driver.quit()

@pytest.fixture
def login(driver):
    Features.login(driver)
    return driver

@pytest.fixture(scope="session")
def company_name():
    return TestData.CompanyProfileValid.COMPANY_NAME()
