import logging
import os.path

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from urllib3.exceptions import MaxRetryError
from webdriver_manager.chrome import ChromeDriverManager

from core.selenium.web_drivers.idriver import IDriver
import json

logger = logging.getLogger(__name__)


class Chrome(IDriver):
    """
    Handles Chrome driver initialization.
    """

    __ROOT_DIR = os.path.dirname(os.path.abspath("readme.md"))

    def init_driver(self):
        """
        Initializes Chrome driver.

        :return: A new ChromeDriver.
        """
        chrome_pref = {}
        chrome_pref.setdefault("profile.default_content_settings.popups", 0)
        chrome_pref.setdefault("download.prompt_for_download", False)
        chrome_pref.setdefault("profile.content_settings.exceptions.automatic_downloads.*.setting", 1)
        chrome_pref.setdefault("safebrowsing.enabled", True)

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", chrome_pref)
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("ignore-certificate-errors")
        options.add_argument("--start-maximized")
        # options.add_argument("headless")

        capabilities = webdriver.DesiredCapabilities().CHROME
        capabilities["acceptSslCerts"] = True
        capabilities["acceptInsecureCerts"] = True
        capabilities["goog:chromeOptions"] = options

        return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
