import pytest
import config
from pages.communication_ai_ad_copy_optimization_page import AdCopyOptimizationPage
from pages.google_meta_integration_page import LandingPage
from pages.login_page import LoginPage
from tests.conftest import setup

@pytest.mark.parametrize("username, password, otp, description", [
    (config.USERNAME, config.PASSWORD, config.OTP, "Verify UI elements in Ad Copy Optimization page."),
], ids=[
    "Verify UI elements in Ad Copy Optimization page."
])

def test_verify_communication_ai_ad_copy_optimization_elements(setup, username, password, otp, description):
    print(f"Running Test: {description}")
    login_page = LoginPage(setup)
    login_page.open_url(config.BASE_URL)
    login_page.login(username, password)
    login_page.submit_otp(otp)
    communication_ai_page = AdCopyOptimizationPage(setup)
    communication_ai_page.navigate_to_ad_copy_optimization_page()
    communication_ai_page.verify_ui_in_ad_copy_optimization_page()