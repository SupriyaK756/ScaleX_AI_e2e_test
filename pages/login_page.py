from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helper import Helper


class LoginPage(BasePage):
    # Fields
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Enter email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Password']")
    OTP_FIELD = (By.XPATH, "//input[@placeholder='Enter OTP']")

    # Buttons
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    OTP_BUTTON = (By.XPATH, "//button[text()='Verify OTP']")

    # Error messages
    ERROR_MESSAGES = {
        "invalid_credentials": (By.XPATH, "//div[text()='Invalid Credentials']"),
        "invalid_otp": (By.XPATH, "//div[text()='Invalid OTP']"),
        "invalid_email": (By.XPATH, "//*[text()='Please enter a valid email address.']"),
        "missing_email": (By.XPATH, "//div[text()='Email is required.']"),
        "missing_password": (By.XPATH, "//div[text()='Password is required.']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.helper = Helper(driver)

    # Actions
    def enter_username(self, username):
        self.helper.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.helper.send_keys(self.PASSWORD_FIELD, password)

    def enter_otp(self, otp):
        self.helper.send_keys(self.OTP_FIELD, otp)

    def click_login(self):
        self.helper.click(self.LOGIN_BUTTON)

    def click_otp(self):
        self.helper.click(self.OTP_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def submit_otp(self, otp):
        self.enter_otp(otp)
        self.click_otp()

    # Verifications
    def verify_error_message(self, error_type):
        assert self.helper.is_element_visible(self.ERROR_MESSAGES[error_type]) is True,\
            f"{error_type} message not visible"

    def verify_missing_fields(self, username, password):
        if not username:
            self.verify_error_message("missing_email")
        if not password:
            self.verify_error_message("missing_password")

