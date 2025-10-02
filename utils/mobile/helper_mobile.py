from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import allure


@allure.step("Wait for element {locator} to be visible (timeout={timeout}s)")
def wait_for_element(driver, locator, timeout=15):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

@allure.step("Wait for element {locator} and click (timeout={timeout}s)")
def wait_and_click(driver, locator, timeout=15):
    el = wait_for_element(driver, locator, timeout)
    el.click()
    return el

@allure.step("Wait for element {locator} and send keys: {text} (timeout={timeout}s)")
def wait_and_send_keys(driver, locator, text, timeout=15):
    el = wait_for_element(driver, locator, timeout)
    el.clear()
    el.send_keys(text)
    return el

def scroll_to_element(driver, locator):
    for _ in range(5):
        try:
            return driver.find_element(*locator)
        except:
            driver.swipe(500, 1500, 500, 500, 800)  # swipe up
    raise Exception(f"Element {locator} not found after scrolling")

from appium.webdriver.common.touch_action import TouchAction

def draw_signature(driver, element):
    action = TouchAction(driver)
    location = element.location
    size = element.size

    start_x = location['x'] + size['width'] * 0.2
    start_y = location['y'] + size['height'] * 0.5
    end_x = location['x'] + size['width'] * 0.8
    end_y = start_y

    action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

