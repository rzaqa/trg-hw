import json
import os
import re

import allure
import requests
from playwright.sync_api import Page, expect

from .base_page import BasePage


class LifeAtTrgPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.section_header = page.get_by_text("#Life At TRG|TRG Careers")
        self.core_value_blocks = page.locator(
            ".elementor-element.elementor-widget-container"
        )
        self.image_elements = page.locator("img[src*='uploads']")
        self.core_value_sections = page.locator("div[data-testid='columns']")
        self.first_core_value = page.get_by_text("We work together.")

        self.core_values = []
        for i in range(1, 5):
            poster_alt = f"Poster {i}.jpg"
            container = page.locator(
                f"xpath=//img[@alt='{poster_alt}']/ancestor::div[@data-testid='mesh-container-content'][1]"  # noqa: E501
            )
            self.core_values.append(
                {
                    "poster": page.locator(f"img[alt='{poster_alt}']"),
                    "header": container.locator(
                        "xpath=.//div[@data-testid='richTextElement'][1]"
                    ),
                    "text": container.locator(
                        "xpath=.//div[@data-testid='richTextElement'][2]"
                    ),
                }
            )

    @allure.step("Scroll to a first core value")
    def scroll_to_core_values(self):
        self.first_core_value.scroll_into_view_if_needed()
        expect(self.first_core_value).to_be_visible(timeout=2000)

        # Take a screenshot for verification after a 0.1 pause
        self.page.wait_for_timeout(100)
        allure.attach(
            self.page.screenshot(full_page=False),
            name="Scrolled to Core Values",
            attachment_type=allure.attachment_type.PNG,
        )

    @allure.step("Verify all 4 core values are visible")
    def verify_core_values_visible(self):
        """Check that exactly 4 core value columns are present."""
        count = self.core_value_sections.count()
        assert count == 4, f"Expected 4 core value sections, but found {count}"
        for i in range(count):
            expect(self.core_value_sections.nth(i)).to_be_visible()

    @allure.step("Extract and save Core Values to JSON file")
    def save_core_values_to_json(self, output_path: str = "core_values.json"):
        data = []
        for _, v in enumerate(self.core_values, start=1):
            headline = v["header"].inner_text().strip()
            description = v["text"].inner_text().strip()
            image_url = v["poster"].get_attribute("src")
            data.append(
                {
                    "headline": headline,
                    "description": description,
                    "image_url": image_url,
                }
            )

        abs_path = os.path.abspath(output_path)
        with open(abs_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        allure.attach.file(
            abs_path,
            name="Core Values JSON",
            attachment_type=allure.attachment_type.JSON,
        )
        print(f"✅ Core values saved to: {abs_path}")
        return data

    @allure.step("Count total exclamation marks in all Core Value descriptions")
    def count_exclamation_marks(self, core_values):
        """Count total exclamation marks across all core value descriptions."""
        total_marks = sum(v["description"].count("!") for v in core_values)

        print(f"\n❗ Total exclamation marks found: {total_marks}")
        allure.attach(
            str(total_marks),
            name="Total Exclamation Marks",
            attachment_type=allure.attachment_type.TEXT,
        )

        return total_marks

    @allure.step("Download all Core Value images and rename by headline")
    def download_core_value_images(
        self, core_values, download_dir: str = "downloads/core_values"
    ):
        """Download all images and rename them according to their headlines."""
        os.makedirs(download_dir, exist_ok=True)

        for _, value in enumerate(core_values, start=1):
            image_url = value["image_url"]
            headline = value["headline"]
            safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", headline).strip("_")
            filename = f"{safe_name}.jpg"
            filepath = os.path.join(download_dir, filename)

            # Download image via requests
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            with open(filepath, "wb") as f:
                f.write(response.content)

            allure.attach.file(
                filepath,
                name=f"Image - {headline}",
                attachment_type=allure.attachment_type.PNG,
            )
            print(f"🖼️  Saved: {filepath}")

        print(f"\n✅ All images downloaded to: {os.path.abspath(download_dir)}")
