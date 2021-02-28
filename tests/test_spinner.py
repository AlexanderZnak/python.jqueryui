from pages.demos_page import DemosPage
from pages.spinner_page import SpinnerPage


def test_popup_should_be_appeared_with_entered_value_after_get_value_in_spinner_from_widgets(browser, screenshot):
    demos_page = DemosPage(browser)
    spinner_page = SpinnerPage(browser)
    widget_name = "Spinner"
    section_name = "Widgets"
    number = 1

    # Arrange
    demos_page \
        .open_page() \
        .click_by_exact_widget_from_section(section_name, widget_name)

    # Act
    spinner_page \
        .switch_to_frame() \
        .fill_in_search_a_value_field(number) \
        .click_get_value()

    # Assert
    assert spinner_page.get_value_from_appeared_popup() == number, f"Popup should contain entered value: {number}"
