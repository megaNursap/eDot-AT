from appium.webdriver.common.appiumby import AppiumBy

class DocumentLocators:
    ALLOW_CAMERA = (AppiumBy.ID, "id.edot.ework:id/btn_positive")
    ALLOW_EDOT_ACCESS_CAMERA = (AppiumBy.ID, "android:id/button1")
    ALLOW_TAKE_PICTURE = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button")
    KTP_INPUT = (AppiumBy.ID, "id.edot.ework:id/etInput")
    BTN_OPEN_CAMERA = (
        AppiumBy.XPATH,
        "//android.widget.ScrollView//androidx.recyclerview.widget.RecyclerView//android.widget.Button"
    )
    BTN_CAPTURE = (AppiumBy.ID, "id.edot.ework:id/btn_capture")
    SUBMIT_BUTTON = (
        AppiumBy.XPATH,
        "//android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.Button"
    )
