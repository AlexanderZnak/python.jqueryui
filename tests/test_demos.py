import pytest

from pages.demos_page import DemosPage


@pytest.mark.parametrize("section_name", ["Interactions", "Widgets", "Effects", "Utilities"])
def test_menu_bar_should_contain_interactions_widgets_effects_utilities_sections(browser, screenshot, section_name):
    # Arrange
    demos_page = DemosPage(browser)

    # Act
    demos_page.open_page()

    # Assert
    assert demos_page.is_bar_menu_section_exist(
        section_name) is True, f"Bar menu should contain section: {section_name}"
