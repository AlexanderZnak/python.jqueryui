from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    _TAGS_FIELD = (By.ID, "tags")

    def fill_in_tags_field(self, search_text):
        self.find_element(self._TAGS_FIELD).send_keys(search_text)
        return self

    def select_necessary_suggested_search(self, suggested_text):
        element = self.find_element(self._TAGS_FIELD)
        while element.get_attribute("value") != suggested_text:
            element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def get_value_from_tags(self):
        return self.find_element(self._TAGS_FIELD).get_attribute("value")
