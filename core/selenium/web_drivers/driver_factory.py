import yaml

from core.selenium.web_drivers.chrome import Chrome
from core.selenium.web_drivers.firefox import FireFox


class DriverFactory:
    """
    Returns the correct instance of the driver.
    """

    __FIREFOX = "firefox"
    __CHROME = "chrome"

    def __init__(self, web_driver_config):
        """
        Initializes the driver factory.
        """
        self.__config_data = yaml.safe_load(open("environment.yml"))
        self._config = web_driver_config

    def get_driver(self):
        """
        Gets the correct instance of IWebDriver according the name given by parameter.

        :return: The instance of web driver.
        """
        strategy_browser = {self.__FIREFOX: FireFox(), self.__CHROME: Chrome()}
        return strategy_browser.get(self._config.get_browser().lower()).init_driver()
