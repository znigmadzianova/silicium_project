from pages.registration_page import RegistrationPage
import pytest
import time

LINK = 'https://demoqa.com/automation-practice-form'

def test_fill_registration_data(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open_page(LINK)
    registration_page.fill_personal_data()
    registration_page.fill_additional_data()
    del registration_page
    time.sleep(1)

@pytest.mark.xfail(reason='Registration was not successful')
def test_check_registration_message(browser):
    registration_page = RegistrationPage(browser)
    registration_page.check_registration_message()
    del registration_page

@pytest.mark.xfail(reason='There is difference in data')
def test_check_registration_data(browser):
    registration_page = RegistrationPage(browser)
    registration_page.check_registration_message()
    del registration_page