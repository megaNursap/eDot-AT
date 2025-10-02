import datetime
class TestDataMobile:
    class LoginValid:
        COMPANY_ID = "5049209"
        COMPANY_EMAIL = "qatestsalesman"
        COMPANY_PASSWORD = "it.QA2025"

    class OutletProfileValid:
        def outlet_name():
            now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")  
            return f"Outlet QA Automation {now}"
        OUTLET_ADDRESS = "Jl. Example No.123, Jakarta"
        OUTLET_PHONE = "08123456789"
        OUTLET_EMAIL = "qa.automation@test.com"
        OUTLET_CONTACT_PERSON = "QA Tester"
        OUTLET_ADDRESS = "Jl. QA Automation No.1"