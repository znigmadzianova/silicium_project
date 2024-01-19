from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser):
        self.browser = browser

    def is_element_clickable(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def open_page(self, link):
        self.browser.get(link)