import logging

from behave import use_fixture

from core.selenium.fixtures import selenium_browser
from tests.features.logging import setup as setup_logging

logger = logging.getLogger(__name__)


def before_all(context):
    setup_logging()


def before_feature(context, feature):
    use_fixture(selenium_browser, context)

