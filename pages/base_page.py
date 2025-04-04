from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        """ Opens a given URL """
        self.driver.get(url)

    def send_keys(self, locator, text):
        """ Enters text into an input field """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        """ Clicks an element """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_title(self):
        """ Returns the current page title """
        return self.driver.title
