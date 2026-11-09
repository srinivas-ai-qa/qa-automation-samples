import pytest

from pages.login_page import LoginPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"


def test_valid_login_opens_inventory(driver):
    page = LoginPage(driver).open().login(VALID_USER, VALID_PASSWORD)
    assert page.is_inventory_visible()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", VALID_PASSWORD, "Epic sadface: Sorry, this user has been locked out."),
        (VALID_USER, "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
        ("", VALID_PASSWORD, "Epic sadface: Username is required"),
    ],
    ids=["locked-out-user", "wrong-password", "missing-username"],
)
def test_invalid_login_shows_error(driver, username, password, expected_error):
    page = LoginPage(driver).open().login(username, password)
    assert page.error_message() == expected_error
