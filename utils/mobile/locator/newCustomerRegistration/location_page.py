from selenium.webdriver.common.by import By

class NewCustomerLocationLocators:
    ADDRESS_TYPE = (By.ID, "id.edot.ework:id/et_address_type")
    ADDRESS_TYPE_OPTION = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView"
    )

    ADDRESS_INPUT = (By.ID, "id.edot.ework:id/etAddress")

    # Province
    PROVINCE_INPUT = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.EditText"
    )
    PROVINCE_FIRST = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView"
    )

    # City
    CITY_INPUT = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.EditText"
    )
    CITY_FIRST = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView"
    )

    # District
    DISTRICT_INPUT = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.EditText"
    )
    DISTRICT_FIRST = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView"
    )

    # Sub-district
    SUBDISTRICT_INPUT = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.EditText"
    )
    SUBDISTRICT_FIRST = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView"
    )

    # Postal code
    POSTALCODE_INPUT = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.EditText"
    )
    POSTALCODE_FIRST_OPTION = (By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.TextView"
    )

    LONGITUDE = (By.ID, "id.edot.ework:id/et_longitude")
    LATITUDE = (By.ID, "id.edot.ework:id/et_latitude")

    BUTTON_CONTINUE = (By.XPATH,
        "//android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.Button"
    )
