# QA automation samples

Sample code showing a Pytest and Selenium framework, data-driven tests, Allure reporting, and a Locust load test. It runs against public demo sites, so it contains no employer code or data.

## What's inside

- `pages/login_page.py`: Page Object Model for the login page
- `tests/test_login.py`: UI tests, including data-driven cases
- `conftest.py`: headless Chrome fixture
- `locustfile.py`: Locust load test against a public REST API
- `.github/workflows/tests.yml`: runs the tests on every push and pull request, and uploads Allure results

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the UI tests

```bash
pytest
```

Allure results are written to `allure-results/`. To view the report, install the Allure CLI and run `allure serve allure-results`.

## Run the load test

```bash
locust -f locustfile.py --headless -u 5 -r 1 -t 1m
```

Sites used: [saucedemo.com](https://www.saucedemo.com/) (UI) and [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/) (API).
