from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helper import Helper


class ContextualIdeation(BasePage):
    CONTEXTUAL_IDEATION_PAGE_UI_ELEMENTS = \
        {
        "MESSAGE_COMMUNICATION_AI": (By.XPATH, "//input[@placeholder='Message Communication AI']"),
        "CONTEXTUAL_IDEATION_TEXT": (By.XPATH, "//h2[text()='Contextual Ideation']"),
        "SUBMIT_BUTTON": (By.XPATH, "//button[@type='submit']")
        }

    NAVIGATE_TO_CONTEXTUAL_IDEATION = \
        {
        "COMMUNICATION_AI": (By.XPATH, "//p[text()='Communication AI']"),
        "CONTEXTUAL_IDEATION": (By.XPATH, "//a[text()='Contextual Ideation']"),

        }

    def __init__(self, driver):
        super().__init__(driver)
        self.helper = Helper(driver)


    def navigate_to_contextual_ideation_page(self):
        for name, locator in self.NAVIGATE_TO_CONTEXTUAL_IDEATION.items():
            assert self.helper.is_element_visible(locator) is True, \
                f"{name} is not visible"
            self.click(locator)

    def verify_ui_in_contextual_ideation_page(self):
        for name, locator in self.CONTEXTUAL_IDEATION_PAGE_UI_ELEMENTS.items():
            print(name, locator)
            assert self.helper.is_element_visible(locator) is True, \
            f"{name} with locator {locator} is not visible"