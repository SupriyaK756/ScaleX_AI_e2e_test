from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helper import Helper


class LandingPage(BasePage):
    LANDING_PAGE_UI_ELEMENTS = \
        {
        "GOOGLE_ADS_INTEGRATION": (By.XPATH, "//div[@class='main-title mt-4']"),
        "INTEGRATE_GOOGLE_ADS": (By.XPATH, "//b[text() = 'Integrate Google Ads']"),
        "CONNECT_GOOGLE_ADS_ACCOUNT": (
        By.XPATH, "//div[text() = 'Connect Google Ads Account with Shopify to get started.']"),
        "INTEGRATE_FACEBOOK_ADS": (By.XPATH, "//b[text() = 'Integrate Facebook Ads']"),
        "CONNECT_FACEBOOK_ADS_ACCOUNT": (
        By.XPATH, "//div[text() = 'Connect Facebook Ads Account with Shopify to get started.']"),
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.helper = Helper(driver)

    def verify_landing_page(self):
        for name, locator in self.LANDING_PAGE_UI_ELEMENTS.items():
            assert self.helper.is_element_visible(locator) is True, \
                f"{name} with locator {locator} is not visible"
