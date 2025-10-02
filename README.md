# How to install
run this command = make -f Makefile install

# How to run one file
make -f Makefile allure-report FILE=tests/mobile/test_m_login_001.py

# How to Run ALl
make -f Makefile allure-report

# How to see the Result
1. allure serve allure-results