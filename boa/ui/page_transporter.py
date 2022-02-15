import logging

from core.selenium.web_driver_manager import WebDriverManager

logger = logging.getLogger(__name__)


class PageTransporter:
    """
    Handles Page transporter to navigate to different urls in the application.
    """

    def __init__(self, web_driver_manager):
        """
        Initializes PageTransporter.
        """
        logger.info("Initialize Page Transporter")
        self.web_driver = web_driver_manager.get_web_driver()

    def navigate_to_boa(self):
        url = "https://www.boa.bo/BoAWebsite"
        self.web_driver.get(url)
