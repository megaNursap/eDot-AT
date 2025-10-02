from selenium.webdriver.common.by import By

class HomeLocators:
    LOGO = (By.ID, "id.edot.ework:id/img_ework")

    MASTER_OUTLET = (
        By.XPATH, 
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.GridView/android.view.ViewGroup[3]"
    )
    NEW_CUSTOMER = (
        By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.GridView/android.view.ViewGroup[5]"
    )
    
    BACK_ARROW_HEADER = (By.ID, "id.edot.ework:id/imgBackArrowHeader")

    MENU_DRAWER = (By.ID, "id.edot.ework:id/imgDrawer")
    LOGOUT = (By.ID, "id.edot.ework:id/nav_logout")
