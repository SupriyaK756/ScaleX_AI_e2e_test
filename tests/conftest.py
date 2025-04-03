import pytest
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    """ Add command-line options for browser and headless mode """
    parser.addoption("--browser", action="store", default=config.BROWSER, help="Choose browser: chrome, firefox, edge")
    parser.addoption("--headless", action="store", type=str, default=str(config.HEADLESS).lower(),
                     help="Run tests in headless mode (true/false)")


@pytest.fixture(scope="function")
def setup(request):
    """ Selenium WebDriver Fixture for test setup """
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless").lower() == "true"

    if browser.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    elif browser.lower() == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    else:
        raise ValueError("Invalid browser choice! Use --browser=chrome, firefox, or edge.")

    driver.implicitly_wait(config.IMPLICIT_WAIT)  # Use wait time from config
    yield driver  # Provide driver instance to test
    driver.quit()  # Cleanup after test
