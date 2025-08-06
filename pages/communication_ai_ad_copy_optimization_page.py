from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helper import Helper

class AdCopyOptimizationPage(BasePage):
    AD_COPY_OPTIMIZATION_UI_ELEMENTS_PAGE = \
        {
        "AD_COPY_OPTIMIZATION": (By.XPATH, "//h2[text()='Ad Copy Optimizations']"),
        "APPLY_BUTTON": (By.XPATH, "//button[text()='Apply']")
        }

    NAVIGATE_TO_AD_COPY_OPTIMIZATION = \
        {
        "COMMUNICATION_AI": (By.XPATH, "//p[text()='Communication AI']"),
        "AD_COPY_OPTIMIZATION": (By.XPATH, "//a[text()='Ad Copy Optimizations']"),
        }

    def __init__(self, driver):
        super().__init__(driver)
        self.helper = Helper(driver)

    def navigate_to_ad_copy_optimization_page(self):
        for name, locator in self.NAVIGATE_TO_AD_COPY_OPTIMIZATION.items():
            assert self.helper.is_element_visible(locator) is True, \
                f"{name} is not visible"
            self.click(locator)

    def verify_ui_in_ad_copy_optimization_page(self):
        for name, locator in self.AD_COPY_OPTIMIZATION_UI_ELEMENTS_PAGE.items():
            print(name, locator)
            assert self.helper.is_element_visible(locator) is True, \
            f"{name} with locator {locator} is not visible"
