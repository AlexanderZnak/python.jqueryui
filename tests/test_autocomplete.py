from pages.autocomplete_page import AutoCompletePage
from pages.demos_page import DemosPage


def test_auto_complete_should_suggest_pertain_search_text_and_search_it_after_necessary_choice(browser, screenshot):
    demos_page = DemosPage(browser)
    autocomplete_page = AutoCompletePage(browser)
    widget_name = "Autocomplete"
    section_name = "Widgets"
    search_text = "a"
    suggested_text = "Asp"

    # Arrange
    demos_page \
        .open_page() \
        .click_by_exact_widget_from_section(section_name, widget_name)

    # Act
    autocomplete_page \
        .switch_to_frame() \
        .fill_in_tags_field(search_text) \
        .select_necessary_suggested_search(suggested_text)

    # Assert
    assert autocomplete_page.get_value_from_tags() == suggested_text, f"Tags should contain suggested search: " \
                                                                      f"{suggested_text}"
