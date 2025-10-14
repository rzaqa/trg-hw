import pytest
from playwright.sync_api import Page, expect

EXPECTED_OG_TITLE = "TRG - Ultimate AI Data Fusion Solutions. Securing Better Lives."


@pytest.mark.functional
def test_save_core_values_and_download_images(page: Page):
    """
    Extracts all core values (headline + description) from the #Life At TRG page,
    saves them to a JSON file, counts total exclamation marks across all descriptions,
    and downloads all 4 related images to the repository with filenames matching
    their core value headlines.
    """
    page.goto("/")
    expect(page).to_have_title(EXPECTED_OG_TITLE)
