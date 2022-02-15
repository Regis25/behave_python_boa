import abc
from core.selenium.tools.web_driver_tools import WebDriverTools


class BasePage:

    def __init__(self, web_driver_manager):
        self.driver = web_driver_manager.get_web_driver()
        self.wait = web_driver_manager.get_wait()
        self.driver_tool = WebDriverTools(web_driver_manager)
        self.wait_until_page_object_is_loaded()

    @abc.abstractmethod
    def wait_until_page_object_is_loaded(self):
        pass


