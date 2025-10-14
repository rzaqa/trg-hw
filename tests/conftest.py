import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from playwright_config import config

load_dotenv()


@pytest.fixture(scope="session")
def env_type():
    """Returns the current environment type (local or CI)."""
    return os.getenv("ENV_TYPE", config["env_type"])


@pytest.fixture(scope="session", params=config["browsers"])
def browser(request):
    """Launch each browser type (chromium, firefox, webkit) once per session."""
    browser_name = request.param
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=config["headless"])
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    """Creates a new page with base_url from config."""
    context = browser.new_context(base_url=config["base_url"])
    page = context.new_page()
    yield page
    context.close()
