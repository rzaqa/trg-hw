import allure
import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.life_at_trg_page import LifeAtTrgPage
from playwright_config import config


@allure.feature("Core Values")
@allure.story("Prepare Core Values Data")
@pytest.mark.functional
def test_save_core_values_and_download_images(page: Page):
    """
    Extracts all core values (headline + description) from the #Life At TRG page,
    saves them to a JSON file, counts total exclamation marks across all descriptions,
    and downloads all 4 related images to the repository with filenames matching
    their core value headlines.
    """
    home = HomePage(page)

    with allure.step("Open homepage"):
        home.open_homepage()

    with allure.step("Verify homepage title and OG tag"):
        home.verify_page_loaded_by_url(config["base_url"])

    with allure.step("Navigate to Careers page (new tab)"):
        careers_page = home.go_to_career_page()
        careers_page.verify_page_loaded_by_url(config["careers_url"])

    with allure.step("Navigate to #Life at TRG section"):
        careers_page.go_to_life_at_trg()
        life_page = LifeAtTrgPage(careers_page.page)
        life_page.verify_page_loaded_by_url(config["life_at_trg_url"])

    with allure.step("Scroll to and verify Core Values section"):
        life_page.scroll_to_core_values()
        life_page.verify_core_values_visible()

    with allure.step("Extract and save all Core Values to JSON"):
        core_values = life_page.save_core_values_to_json()

    with allure.step("Count total exclamation marks"):
        total_exclaims = life_page.count_exclamation_marks(core_values)
        assert total_exclaims > 0, "Expected at least one exclamation mark!"

    with allure.step("Download Core Value images and rename by headline"):
        life_page.download_core_value_images(core_values)
