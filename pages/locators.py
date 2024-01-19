from selenium.webdriver.common.by import By
import json


class RegistrationPageLocators():
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    MOBILE = (By.XPATH, '//input[@id="userNumber"]')
    DATE_OF_BIRTH = (By.ID, 'dateOfBirthInput')
    SUBJECTS = (By.ID, 'subjectsInput')
    PICTURE = (By.CSS_SELECTOR, '#uploadPicture')
    ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    SUBMIT = (By.ID, 'submit')
    STATE_LIST = (By.ID, 'state')
    CITY_LIST = (By.ID, 'city')
    FOOTER = (By.TAG_NAME, 'footer')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "modal-title")]')
    TABLE_DATA = (By.XPATH, '/tbody/tr')
    ROW_DATA = (By.TAG_NAME, 'td')
    GENDER_TITLE = (By.XPATH, '//div[contains(text(), "Gender")]')
    HOBBIES_TITLE = (By.XPATH, '//label[contains(text(), "Hobbies")]')
    MONTHS_LIST = (By.XPATH, '//select[@class="react-datepicker__month-select"]')
    YEARS_LIST = (By.XPATH, '//select[@class="react-datepicker__year-select"]')
