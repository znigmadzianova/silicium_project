from .base_page import BasePage
from .locators import RegistrationPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import json
import os
from .helper import transform_data_to_website_format, get_keys_from_dict

with open('config.json', 'r') as f:
    testing_data = json.load(f)

root_dir = os.getcwd()
file_path = os.path.join(root_dir, testing_data['picture'])

input_data = transform_data_to_website_format( testing_data )

class RegistrationPage(BasePage):
    def fill_personal_data(self):

        if self.is_element_clickable(*RegistrationPageLocators.FIRST_NAME):
            first_name = self.browser.find_element(*RegistrationPageLocators.FIRST_NAME)
            first_name.send_keys(testing_data['first_name'])

            last_name = self.browser.find_element(*RegistrationPageLocators.LAST_NAME)
            last_name.send_keys(testing_data['last_name'])

            email = self.browser.find_element(*RegistrationPageLocators.EMAIL)
            email.send_keys(testing_data['email'])

            gender = get_keys_from_dict(testing_data['gender'])[0]
            place_to_move = self.browser.find_element(*RegistrationPageLocators.GENDER_TITLE)
            ActionChains(self.browser).move_to_element(place_to_move).perform()
            gender_to_choose = self.browser.find_element(By.XPATH, \
                             f'//label[contains(text(), "{gender}") and contains(@for, "gender")]')
            gender_to_choose.click()

            mobile = self.browser.find_element(*RegistrationPageLocators.MOBILE)
            mobile.send_keys( testing_data['mobile'] )

            date_of_birth = self.browser.find_element(*RegistrationPageLocators.DATE_OF_BIRTH)
            date_of_birth.click()
            months_select = Select(self.browser.find_element(*RegistrationPageLocators.MONTHS_LIST))
            months_select.select_by_visible_text(testing_data['date_of_birth'].split()[1])
            years_select = Select(self.browser.find_element(*RegistrationPageLocators.YEARS_LIST))
            years_select.select_by_visible_text(testing_data['date_of_birth'].split()[2])
            day_to_choose = testing_data['date_of_birth'].split()[0]
            day_select = self.browser.find_element(By.XPATH, \
                                                   f'//div[contains(@class, "day--0{day_to_choose}") and not(contains(@class, "outside-month"))]')
            day_select.click()

        else:
            print('The data is not relevant. Check the data')


    def fill_additional_data(self):

        footer = self.browser.find_element(*RegistrationPageLocators.FOOTER)
        self.browser.execute_script("arguments[0].style.display = 'none';", footer)

        submit_button = self.browser.find_element(*RegistrationPageLocators.SUBMIT)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

        subjects = self.browser.find_element(*RegistrationPageLocators.SUBJECTS)
        for subject in testing_data['subjects']:
            subjects.send_keys(subject)
            subjects.send_keys(Keys.ENTER)

        submit_button = self.browser.find_element(*RegistrationPageLocators.SUBMIT)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

        hobbies = get_keys_from_dict(testing_data['hobbies'])
        place_to_move = self.browser.find_element(*RegistrationPageLocators.HOBBIES_TITLE)
        for el in hobbies:
            ActionChains(self.browser).move_to_element(place_to_move).perform()
            hobby_to_choose = self.browser.find_element(By.XPATH, \
                            f'//label[contains(text(), "{el}") and contains(@for, "hobbies")]')
            hobby_to_choose.click()

        picture_to_choose = self.browser.find_element(*RegistrationPageLocators.PICTURE)
        picture_to_choose.send_keys(file_path)

        current_address = self.browser.find_element(*RegistrationPageLocators.ADDRESS)
        current_address.send_keys(testing_data['address'])

        state_list = self.browser.find_element(*RegistrationPageLocators.STATE_LIST)
        state_list.click()
        state = testing_data['state']
        state_to_choose = self.browser.find_element(By.XPATH, \
                f'//div[contains(text(), "{state}") and contains(@class, "option")]')
        state_to_choose.click()

        city_list = self.browser.find_element(*RegistrationPageLocators.CITY_LIST)
        city_list.click()
        city = testing_data['city']
        city_to_choose = self.browser.find_element(By.XPATH, \
                f'//div[contains(text(), "{city}") and contains(@class, "option")]')
        city_to_choose.click()

        self.browser.execute_script("arguments[0].click();", submit_button)


    def check_registration_message(self):

        message = self.browser.find_element(*RegistrationPageLocators.SUCCESS_MESSAGE).text
        assert testing_data['success_message'].lower() == message.lower(), 'Registration was not successful'


    def check_registration_data(self):

        output_data = []
        table_rows = self.browser.find_elements(*RegistrationPageLocators.TABLE_DATA)
        for row in table_rows:
            row_data = row.find_element(*RegistrationPageLocators.ROW_DATA)[2].text()
            output_data.append(row_data)

        assert input_data == output_data, 'Data is different'












