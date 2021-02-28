from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SpinnerPage(BasePage):
    _SELECT_A_VALUE_FIELD = (By.ID, "spinner")
    _GET_VALUE_BUTTON = (By.ID, "getvalue")

    def fill_in_search_a_value_field(self, number):
        self.find_element(self._SELECT_A_VALUE_FIELD).send_keys(number)
        return self

    def click_get_value(self):
        self.find_element(self._GET_VALUE_BUTTON).click()

    def get_value_from_appeared_popup(self):
        return int(Alert(self.driver).text)
