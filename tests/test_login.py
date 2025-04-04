import pytest
import config
from pages.login_page import LoginPage


@pytest.mark.parametrize("username, password, expected_title, description", [
    (config.USERNAME, config.PASSWORD, "Dashboard", "Valid login test case with valid username and password"),
    ("invalid_user", "wrong_password", "Login", "Invalid login test case with invalid username and password"),
])
def test_login(setup, username, password, expected_title, description):
    print(f"\nRunning Test: {description}")  # Prints the test description
    login_page = LoginPage(setup)
    login_page.open_url(config.BASE_URL)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    # assert expected_title in login_page.get_title()
