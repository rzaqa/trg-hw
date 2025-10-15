import allure
from playwright.sync_api import Page, expect

from .base_page import BasePage


class CareerPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.life_at_trg_link = page.get_by_role("link", name="#Life at TRG")

    @allure.step("Open 'Life at TRG' page")
    def go_to_life_at_trg(self):
        expect(self.life_at_trg_link).to_be_visible()
        with self.page.expect_navigation():
            expect(self.life_at_trg_link).to_be_visible()
            self.life_at_trg_link.click()
