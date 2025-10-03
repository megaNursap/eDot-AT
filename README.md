# How to install
make -f Makefile install

# How to run one file
make -f Makefile allure-report FILE=tests/mobile/test_m_login_001.py

# How to Run ALl
make -f Makefile allure-report

# How to see the Result
allure serve allure-results

#############################

| Platform   | Test Case File                               | Feature Covered                     |
| ---------- | -------------------------------------------- | ----------------------------------- |
| **Web**    | `tests/web/test_login_001.py`                | Login to eSuite                     |
| **Web**    | `tests/web/test_register_company_002.py`     | Create New Company & Verify Company |
| **Mobile** | `tests/mobile/test_m_login_001.py`           | Login to Mobile App                 |
| **Mobile** | `tests/mobile/test_m_create_customer_002.py` | Create Customer                     |
