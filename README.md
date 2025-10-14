🧰 Playwright Test Setup & Execution Guide

🧩 1. Create and activate virtual environment

```commandline
python -m venv venv
source venv/bin/activate
```
🧩 2. Install dependencies
```commandline
pip install -r requirements.txt
```

🧩 3. Install Playwright browsers
```commandline
python -m playwright install --with-deps
```

🧩 4. Verify environment
```commandline
which python
which pytest
```

✅ Expected:
```
/Users/<you>/trg-hw/venv/bin/python
/Users/<you>/trg-hw/venv/bin/pytest
```

🧩 5. Run tests
```commandline
pytest -v
```

🧩 6. Generate Allure report
```commandline
allure serve allure-results
```


🧩 7. Manual run in GitHub Actions

You can manually trigger Playwright tests from GitHub → Actions → Playwright Tests → Run workflow
It runs tests in all browsers in headless mode.
