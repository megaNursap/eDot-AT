from selenium.webdriver.common.by import By

class NewCustomerBasicLocators:
    ADD_NEW_CUSTOMER = (By.ID, "id.edot.ework:id/tvRegister")

    OUTLET_NAME = (By.ID, "id.edot.ework:id/et_outlet_name")
    OUTLET_PHONE = (By.ID, "id.edot.ework:id/et_outlet_phone")
    OUTLET_EMAIL = (By.ID, "id.edot.ework:id/et_outlet_email")
    CONTACT_PERSON = (By.ID, "id.edot.ework:id/et_contact_person")

    CHANNEL = (By.ID, "id.edot.ework:id/et_channel")
    CHANNEL_OPTION_MODERN_TRADE = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView"
    )

    OUTLET_TYPE = (By.ID, "id.edot.ework:id/et_outlet_type")
    SEARCH_INPUT = (By.ID, "id.edot.ework:id/etSearch")
    OUTLET_TYPE_GROSIR = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView"
    )

    PRICE_LIST = (By.ID, "id.edot.ework:id/et_pricelist")
    PRICE_LIST_DEFAULT = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView"
    )

    BUTTON_CONTINUE = (By.ID, "id.edot.ework:id/button_text")
