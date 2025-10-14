import os

from dotenv import load_dotenv

# Load .env file only if present (for local development)
load_dotenv()

ENV_TYPE = os.getenv("ENV_TYPE", "local")

# Default base URL (can be overridden via environment variables)
BASE_URL = os.getenv("BASE_URL", "https://www.trgint.com/")

# Headless mode: always True in CI, configurable locally
HEADLESS = True if ENV_TYPE == "CI" else False

# Timeout settings
DEFAULT_TIMEOUT = 10_000  # in milliseconds

# Browsers to run tests on
BROWSERS = ["chromium", "firefox", "webkit"]

# Folder paths
TESTS_DIR = "tests"
REPORTS_DIR = "test-results"

# You can reference these variables in your pytest fixtures or test logic
config = {
    "env_type": ENV_TYPE,
    "base_url": BASE_URL,
    "headless": HEADLESS,
    "browsers": BROWSERS,
    "timeout": DEFAULT_TIMEOUT,
    "tests_dir": TESTS_DIR,
    "reports_dir": REPORTS_DIR,
}
