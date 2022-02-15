import logging
import os.path

from behave import fixture

from core.selenium.web_driver_config import WebDriverConfig
from core.selenium.web_driver_manager import WebDriverManager

logger = logging.getLogger(__name__)


@fixture
def selenium_browser(context):
    ROOT_DIR = os.path.dirname(os.path.abspath("environment.yml"))
    web_driver_config_file_name = os.path.join(ROOT_DIR, "config", "driver_config.json")

    web_driver_config = WebDriverConfig()
    web_driver_config.initialize(web_driver_config_file_name)

    logger.info("-----Start Automation execution for DEMO application-----")
    context.web_driver_manager = WebDriverManager(web_driver_config)
    logger.info(context)

    yield context.web_driver_manager

    logger.info("-----Ends Automation execution for DEMO application-----")
    context.web_driver_manager.quit_driver()
    logger.info(context)
