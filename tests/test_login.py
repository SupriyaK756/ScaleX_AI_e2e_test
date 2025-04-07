import pytest
import config
from pages.login_page import LoginPage


@pytest.mark.parametrize("username, password, otp, expected_error, description", [
    # (config.USERNAME, config.PASSWORD, config.OTP, "Valid_Login", "Valid login test case."),
    (config.USERNAME, config.PASSWORD, "123452", "invalid_otp", "Verify failed login with valid username and password and invalid OTP."),
    (config.USERNAME, "INVALID_PASSWORD", config.OTP, "invalid_credentials", "Verify failed login with valid username and invalid password."),
    ("INVALID_USERNAME@abc.com", "INVALID_PASSWORD", config.OTP, "invalid_credentials", "Verify failed login with invalid username and password."),
], ids=[
    # "Valid_Login",
    "Invalid OTP",
    "Invalid Password",
    "Invalid Username and Password",
])
def test_invalid_login_flows(setup, username, password, otp, expected_error, description):
    print(f"\nRunning Test: {description}")
    login_page = LoginPage(setup)
    login_page.open_url(config.BASE_URL)
    login_page.login(username, password)
    if expected_error == "invalid_otp":
        login_page.submit_otp(otp)

    login_page.verify_error_message(expected_error)


@pytest.mark.parametrize("username, password, description", [
    (config.USERNAME, "", "Password is missing."),
    ("", config.PASSWORD, "Username is missing."),
    ("", "", "Both username and password are missing."),
], ids=[
    "Missing Password",
    "Missing Username",
    "Missing Both Fields",
])
def test_missing_user_inputs(setup, username, password, description):
    print(f"\nRunning Test: {description}")
    login_page = LoginPage(setup)
    login_page.open_url(config.BASE_URL)

    login_page.login(username, password)
    login_page.verify_missing_fields(username, password)
