from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Enter email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")

    def enter_username(self, username):
        """ Enters username """
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        """ Enters password """
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_login(self):
        """ Clicks the login button """
        self.click(self.LOGIN_BUTTON)
