from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from core.selenium.web_drivers.idriver import IDriver


class FireFox(IDriver):
    """
    Handles Firefox driver initialization.
    """

    def init_driver(self):
        """
        Initializes Firefox. driver.
        TODO Add the host to run with docker container -> localhost and gitlab.

        :return: A new FirefoxDriver.
        """
        webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox()
