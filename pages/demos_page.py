from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DemosPage(BasePage):
    _BAR_MENU_SECTION = "//*[contains(@class, 'widget-title') and contains(text(), '{}')]"

    def open_page(self):
        self.driver.get(f"{self.URL}demos/")
        return self

    def is_bar_menu_section_exist(self, section_name):
        try:
            locator = (By.XPATH, self._BAR_MENU_SECTION.format(section_name))
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def click_by_exact_widget_from_section(self, section_name, widget_name):
        widget_locator = f"/following::*[contains(text(),'{widget_name}')]"
        locator = (By.XPATH, f"{self._BAR_MENU_SECTION.format(section_name)}{widget_locator}")
        self.find_element(locator).click()
        return self
