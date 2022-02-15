import json
import logging

import yaml

logger = logging.getLogger(__name__)


class WebDriverConfig:
    """
    Handles the config of web driver.
    """

    # Private Static variables
    __BROWSER = "browser"
    __DRIVER = "web_driver"
    __IMPLICIT_WAIT_TIME = "implicit_wait_time"
    __EXPLICIT_WAIT_TIME = "explicit_wait_time"
    __WAIT_SLEEP_TIME = "wait_sleep_time"

    def __init__(self):
        """
        Initializes the WebDriverConfig.
        """
        with open("environment.yml") as env_file:
            self.__config_data = yaml.safe_load(env_file)
        self.__configReader = None
        self.__browser = None
        self.__implicitWaitTime = None
        self.__explicitWaitTime = None
        self.__waitSleepTime = None

    def initialize(self, web_driver_config_file_name):
        """
        Initializes According the config file.

        :param web_driver_config_file_name: webDriverConfigFilename The configuration parameters.
        """
        logger.info("WebDriverConfig initialize: Read the driver configuration settings")
        with open(web_driver_config_file_name) as f:
            self.__configReader = json.load(f)

        self.__browser = self.__config_data[self.__BROWSER]
        self.__implicitWaitTime = float(self.__configReader[self.__DRIVER][self.__IMPLICIT_WAIT_TIME])
        self.__explicitWaitTime = float(self.__configReader[self.__DRIVER][self.__EXPLICIT_WAIT_TIME])
        self.__waitSleepTime = float(self.__configReader[self.__DRIVER][self.__WAIT_SLEEP_TIME])

    def get_browser(self):
        """
        Gets the browser in which the tests are being executed.

        :return: Browser.
        """
        return self.__browser

    def get_implicit_wait_time(self):
        """
        Gets the implicit wait time set for the WebDriver.

        :return:The implicit wait time.
        """
        return self.__implicitWaitTime

    def get_explicit_wait_time(self):
        """
        Gets the explicit wait time set for the WebDriver.

        :return: The explicit wait time.
        """
        return self.__explicitWaitTime

    def get_wait_sleep_time(self):
        """
        Gets the sleep time wait set for the WebDriver.

        :return: Sleep time wait.
        """
        return self.__waitSleepTime
