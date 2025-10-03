from utils.mobile.locator.home_page import HomeLocators
from utils.mobile.locator.newCustomerRegistration.basic_page import NewCustomerBasicLocators
from utils.mobile.locator.newCustomerRegistration.location_page import NewCustomerLocationLocators
from utils.mobile.locator.newCustomerRegistration.document_page import DocumentLocators
from utils.mobile.locator.newCustomerRegistration.sign_page import SignPageLocators
from utils.mobile.locator.masterOutlet.master_outlet_page import MasterOutletLocators
from selenium.common.exceptions import TimeoutException
from utils.mobile.helper_mobile import (
    wait_and_click,
    wait_and_send_keys,
    wait_for_element,
    scroll_to_element,
    draw_signature,
)
from utils.mobile.features import login_driver
from utils.mobile.test_data_mobile import TestDataMobile
import time



def test_new_customer_registration(login_driver):
    # precondition: logged in
    driver = login_driver

    # Page 1 - Basic
    wait_and_click(driver, HomeLocators.NEW_CUSTOMER)

    wait_and_click(driver, NewCustomerBasicLocators.ADD_NEW_CUSTOMER)

    # generate unique outlet name
    outlet_name = TestDataMobile.OutletProfileValid.outlet_name()
    wait_and_send_keys(driver, NewCustomerBasicLocators.OUTLET_NAME, outlet_name)
    wait_and_send_keys(driver, NewCustomerBasicLocators.OUTLET_PHONE, TestDataMobile.OutletProfileValid.OUTLET_PHONE)
    wait_and_send_keys(driver, NewCustomerBasicLocators.OUTLET_EMAIL, TestDataMobile.OutletProfileValid.OUTLET_EMAIL)
    wait_and_send_keys(driver, NewCustomerBasicLocators.CONTACT_PERSON, TestDataMobile.OutletProfileValid.OUTLET_CONTACT_PERSON)

    wait_and_click(driver, NewCustomerBasicLocators.CHANNEL)
    wait_and_click(driver, NewCustomerBasicLocators.CHANNEL_OPTION_MODERN_TRADE)

    scroll_to_element(driver, NewCustomerBasicLocators.OUTLET_TYPE)

    wait_and_click(driver, NewCustomerBasicLocators.OUTLET_TYPE)
    wait_and_send_keys(driver, NewCustomerBasicLocators.SEARCH_INPUT, "Grosir")
    wait_and_click(driver, NewCustomerBasicLocators.OUTLET_TYPE_GROSIR)

    wait_and_click(driver, NewCustomerBasicLocators.PRICE_LIST)
    wait_and_send_keys(driver, NewCustomerBasicLocators.SEARCH_INPUT, "Default")
    wait_and_click(driver, NewCustomerBasicLocators.PRICE_LIST_DEFAULT)

    wait_and_click(driver, NewCustomerBasicLocators.BUTTON_CONTINUE)

    # Page 2 - Location
    wait_and_click(driver, NewCustomerLocationLocators.ADDRESS_TYPE)
    wait_and_click(driver, NewCustomerLocationLocators.ADDRESS_TYPE_OPTION)

    wait_and_send_keys(driver, NewCustomerLocationLocators.ADDRESS_INPUT, TestDataMobile.OutletProfileValid.OUTLET_ADDRESS)

    # province
    wait_and_click(driver, NewCustomerLocationLocators.PROVINCE_INPUT)
    wait_and_click(driver, NewCustomerLocationLocators.PROVINCE_FIRST)

    scroll_to_element(driver, NewCustomerLocationLocators.DISTRICT_INPUT)

    # city
    wait_and_click(driver, NewCustomerLocationLocators.CITY_INPUT)
    wait_and_click(driver, NewCustomerLocationLocators.CITY_FIRST)

    # district
    wait_and_click(driver, NewCustomerLocationLocators.DISTRICT_INPUT)
    wait_and_click(driver, NewCustomerLocationLocators.DISTRICT_FIRST)

    # subdistrict
    wait_and_click(driver, NewCustomerLocationLocators.SUBDISTRICT_INPUT)
    wait_and_click(driver, NewCustomerLocationLocators.SUBDISTRICT_FIRST)

    # postal code
    wait_and_click(driver, NewCustomerLocationLocators.POSTALCODE_INPUT)
    wait_and_click(driver, NewCustomerLocationLocators.POSTALCODE_FIRST_OPTION)

    wait_and_click(driver, NewCustomerLocationLocators.BUTTON_CONTINUE)

    # Allow access camera
    try:
        wait_and_click(driver, DocumentLocators.ALLOW_CAMERA, timeout=3)
        print("📸 Allowed system camera")
    except TimeoutException:
        print("⚠️ System camera permission not shown")

    try:
        wait_and_click(driver, DocumentLocators.ALLOW_EDOT_ACCESS_CAMERA, timeout=3)
        print("📸 Allowed eDot app access camera")
    except TimeoutException:
        print("⚠️ eDot camera access not shown")

    try:
        wait_and_click(driver, DocumentLocators.ALLOW_TAKE_PICTURE, timeout=3)
        print("📸 Allowed take picture")
    except TimeoutException:
        print("⚠️ Take picture button not shown")


    # Page 3 - Document
    wait_and_send_keys(driver, DocumentLocators.KTP_INPUT, "3501234567890001")

    # Open camera
    wait_and_click(driver, DocumentLocators.BTN_OPEN_CAMERA)

    # Klik tombol capture (ambil foto KTP)
    wait_and_click(driver, DocumentLocators.BTN_CAPTURE)

    # Klik tombol Submit
    wait_and_click(driver, DocumentLocators.SUBMIT_BUTTON)

    # Page 4 - Signature
    wait_and_click(driver,SignPageLocators.SIGNATURE_VIEW)
    signature = wait_for_element(driver, SignPageLocators.SIGNATURE_VIEW)
    draw_signature(driver, signature)

    # Click Register
    wait_and_click(driver, SignPageLocators.BTN_REGISTER)

    time.sleep(3)

    # Confirm popup
    wait_and_click(driver, SignPageLocators.BTN_CONFIRM, timeout=20)

    time.sleep(5)

    # back to home
    wait_and_click(driver, HomeLocators.BACK_ARROW_HEADER, timeout=10)

    # --- Validasi Detail Outlet ---
    wait_and_click(driver, HomeLocators.MASTER_OUTLET, timeout=20)
    wait_and_click(driver, MasterOutletLocators.BTN_SEARCH)
    wait_and_send_keys(driver, MasterOutletLocators.INPUT_SEARCH, outlet_name)  # sesuai input page 1
    wait_and_click(driver, MasterOutletLocators.BTN_SEE_DETAIL)

    # Assert detail outlet
    addr = wait_for_element(driver, MasterOutletLocators.OUTLET_ADDRESS).text
    phone = wait_for_element(driver, MasterOutletLocators.OUTLET_PHONE).text
    email = wait_for_element(driver, MasterOutletLocators.OUTLET_EMAIL).text

    assert addr == TestDataMobile.OutletProfileValid.OUTLET_ADDRESS
    assert phone == "+62"+TestDataMobile.OutletProfileValid.OUTLET_PHONE
    assert email == TestDataMobile.OutletProfileValid.OUTLET_EMAIL
