from appium.webdriver.common.appiumby import AppiumBy

class MasterOutletLocators:
    BTN_SEARCH = (AppiumBy.ID, "id.edot.ework:id/btn_search")
    INPUT_SEARCH = (AppiumBy.ID, "id.edot.ework:id/et_search")
    BTN_SEE_DETAIL = (AppiumBy.ID, "id.edot.ework:id/outlet_action")

    # --- Assert detail ---
    OUTLET_ADDRESS = (AppiumBy.ID, "id.edot.ework:id/tvOutletAddress")
    OUTLET_PHONE = (AppiumBy.ID, "id.edot.ework:id/tvOutletPhone")
    OUTLET_EMAIL = (AppiumBy.ID, "id.edot.ework:id/tvOutletEmail")