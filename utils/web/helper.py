import os
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.step("Wait for element {locator} to be visible (timeout={timeout}s)")
def wait_for_element(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    except Exception as e:
        _attach_screenshot(driver, "wait_for_element_failed")
        raise e


@allure.step("Wait for element {locator} to be clickable (timeout={timeout}s)")
def wait_for_clickable(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    except Exception as e:
        _attach_screenshot(driver, "wait_for_clickable_failed")
        raise e


@allure.step("Wait for text '{text}' in element {locator} (timeout={timeout}s)")
def wait_for_text(driver, locator, text, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
    except Exception as e:
        _attach_screenshot(driver, "wait_for_text_failed")
        raise e


@allure.step("Wait for URL to contain '{text}' (timeout={timeout}s)")
def wait_for_url_contains(driver, text, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.url_contains(text)
        )
    except Exception as e:
        _attach_screenshot(driver, "wait_for_url_contains_failed")
        raise e


@allure.step("Wait for input file element {locator} (timeout={timeout}s)")
def wait_for_input_file(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except Exception as e:
        _attach_screenshot(driver, "wait_for_input_file_failed")
        raise e


def _attach_screenshot(driver, name="screenshot_on_failure"):
    """Helper untuk attach screenshot ke Allure"""
    try:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    except Exception:
        pass


def get_test_file_path(file_name: str) -> str:
    # helper.py → web → utils → project root
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(BASE_DIR, "test_file", file_name)
    file_path = os.path.abspath(file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    return file_path

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def refresh_until_company_visible(driver, locator, retries=5, wait_time=10, delay_between_retries=3):
    for i in range(retries):
        try:
            element = WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable(locator)
            )
            print(f"✅ Element ditemukan setelah {i} refresh")
            return element
        except TimeoutException:
            print(f"🔄 Element belum muncul, refresh ke-{i+1}")
            driver.refresh()
            if i < retries - 1:  # tambahkan delay hanya jika masih ada retry
                time.sleep(delay_between_retries)
    
    raise Exception(f"❌ Element tidak ditemukan setelah {retries} refresh")
