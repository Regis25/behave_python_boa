import logging

from selenium.webdriver.support.ui import WebDriverWait

from core.selenium.web_drivers.driver_factory import DriverFactory

logger = logging.getLogger(__name__)


class WebDriverManager:
    """
    Handles the Web Driver Manager.
    """

    def __init__(self, config):
        """
        Initializes the WebDriverManager.
        """
        self.driver = None
        logger.info("WebDriverManager initialize: Initializing the web driver")
        self.web_driver_config = config
        self.web_driver = DriverFactory(config).get_driver()
        self.web_driver.maximize_window()
        self.web_driver.implicitly_wait(self.web_driver_config.get_implicit_wait_time())
        self.web_driver_wait = WebDriverWait(
            self.web_driver,
            self.web_driver_config.get_explicit_wait_time(),
            self.web_driver_config.get_wait_sleep_time(),
        )

    def get_web_driver(self):
        """
        Gets the WebDriver.

        :return: WebDriver.
        """
        return self.web_driver

    def get_wait(self):
        """
        Gets the WebDriver Wait.

        :return: WebDriverWait.
        """
        return self.web_driver_wait

    def quit_driver(self):
        """
        Closes all the browser instances.
        """
        self.web_driver.quit()
        self.web_driver = None
