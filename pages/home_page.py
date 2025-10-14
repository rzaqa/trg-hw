import allure
from playwright.sync_api import Page, expect

from pages.career_page import CareerPage
from playwright_config import config

from .base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.menu_who_we_are = page.get_by_role("link", name="Who we are")
        self.careers_link = page.get_by_role("link", name="Careers")

    @allure.step("Open TRG home page")
    def open_homepage(self):
        self.open(config["base_url"])

    @allure.step("Open Careers page")
    def go_to_career_page(self):
        self.menu_who_we_are.hover()
        expect(self.careers_link).to_be_visible(timeout=5000)

        with self.page.expect_popup() as popup_info:
            self.careers_link.click(
                force=True
            )  # ensure click works even if slightly offset

        new_page = popup_info.value
        new_page.wait_for_load_state()
        return CareerPage(new_page)
