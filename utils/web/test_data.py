import datetime

class TestData:
    class UserValid:
        VALID_EMAIL = "it.qa@edot.id"
        VALID_PASSWORD = "it.QA2025"
    

    class CompanyProfileValid:
        @staticmethod
        def COMPANY_NAME():
            now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            return f"QA Automation {now}"

        COMPANY_EMAIL = "indo.maju@gmail.com"
        COMPANY_PHONE = "081234567890"
        COMPANY_ADDRESS = "Jl. Merdeka No. 123, Jakarta"
        INDUSTRY_TYPE = "Retail"
        COMPANY_TYPE = "Importer/Exporter"
        LANGUAGE = "English"
        COUNTRY = "Indonesia"
        PROVINCE = "JAWA TIMUR"
        CITY = "KOTA MALANG"
        DISTRICT = "KEDUNGKANDANG"
        SUB_DISTRICT = "SAWOJAJAR"

        EXISTING_COMPANY_NAME = "QA Automation 20251003-023328"

