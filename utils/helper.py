from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Helper:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator, timeout=10):
        """Click an element after waiting for it to be clickable"""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))
            element.click()
        except TimeoutException:
            print(f"Element {by_locator} not clickable")

    def send_keys(self, by_locator, text, timeout=10):
        """Send keys to an element after waiting for visibility"""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"Element {by_locator} not found")

    def get_text(self, by_locator, timeout=10):
        """Get text from an element"""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except TimeoutException:
            print(f"Element {by_locator} not found")
            return None

    def is_element_visible(self, by_locator, timeout=10):
        """Check if an element is visible"""
        try:
            if WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator)):
                print(f"Element {by_locator} visible")
                return True
            else:
                return False
        except TimeoutException:
            return False
