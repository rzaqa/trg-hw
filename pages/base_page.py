import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.URL = None

    @allure.step("Open a given path relative to base_url.")
    def open(self, path: str = "/"):
        self.page.goto(path)

    @allure.step("Verify that the current page has the expected URL.")
    def verify_page_loaded_by_url(self, expected_url=None, timeout=10000):
        url_to_check = expected_url or self.URL
        if not url_to_check:
            raise ValueError("Expected URL not provided or defined in the page object.")
        with allure.step(f"Verify page loaded by URL: {url_to_check}"):
            expect(self.page).to_have_url(url_to_check, timeout=timeout)
