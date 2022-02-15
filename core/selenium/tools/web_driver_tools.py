import logging
import string

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import (
    visibility_of,
    visibility_of_element_located,
)
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


class WebDriverTools:
    """
    Handles the Web Driver tools.
    """

    VALUE_ATTR = "value"

    def __init__(self, web_driver_manager):
        """
        Initializes the WebDriverTools.
        """
        self.driver = web_driver_manager.get_web_driver()
        self.wait = web_driver_manager.get_wait()
        self.action = ActionChains(self.driver)

    def get_page_title(self):
        """
        Gets the Title of the actual Page.

        :return: The title of the page.
        """
        return self.driver.getTitle()

    def clear_text_field(self, web_element):
        """
        Waits and clear the WebElement.

        :param web_element: WebElement to wait and clear.
        """
        self.wait.until(visibility_of(web_element))
        web_element.clear()

    def set_input_field(self, web_element, text=string):
        """
        Sets an Input Field.

        :param web_element: Input WebElement.
        :param text: Text to fill.
        """
        self.wait.until(visibility_of(web_element))
        self.clear_text_field(web_element)
        web_element.send_keys(text)
        if web_element.get_attribute("value") != text:
            self.clear_text_field(web_element)
            web_element.send_keys(text)

    def click_element(self, web_element):
        """
        Waits and click on the WebElement.

        :param web_element: WebElement to wait and click.
        """
        try:
            self.wait.until(visibility_of(web_element))
            self.action.move_to_element(web_element).click().perform()
        except StaleElementReferenceException:
            logger.error("Web element was not found, doing a retry on click element")
            self.action.move_to_element(web_element).click().perform()

    def click_element_by(self, by: By):
        """
        Waits and click on the WebElement.

        :param by: By element.
        """
        try:
            web_element = self.wait_for_clickable_element(by, 3)
            web_element.click()
        except StaleElementReferenceException:
            logger.error("Web element was not found, doing a retry on click element by")
            web_element = self.wait_for_clickable_element(by, 3)
            web_element.click()
        except ElementClickInterceptedException:
            web_element = self.wait_for_clickable_element(by, 3)
            self.click_element_javascript(web_element)

    def click_element_javascript(self, web_element):
        """
        Clicks on the WebElement using Javascript.

        :param web_element: Web element to click.
        """
        self.driver.execute_script("arguments[0].click();", web_element)

    @classmethod
    def select_lst_box_option(cls, web_element, option=str):
        """
        Selects an option from the list box.

        :param web_element: The element to find.
        :param option: Text to select
        """
        select = Select(web_element)
        select.select_by_visible_text(option)

    def get_element_text(self, web_element):
        """
        Waits and gets the text of a WebElement.

        :param web_element: WebElement to wait and get the text.
        :return: Text of the WebElement.
        """
        self.wait.until(visibility_of(web_element))
        return web_element.text

    def set_check_box(self, web_element, value=bool):
        """
        Sets enable or disable the given checkbox.

        :param web_element: Web element to select the checkbox.
        :param value: True or False.
        """
        if value:
            self.select_check_box(web_element)
        else:
            self.clear_check_box(web_element)

    def select_check_box(self, web_element):
        """
        Selects the given checkbox.

        :param web_element: Web element to select the checkbox.
        """
        if not web_element.is_selected():
            self.click_element_javascript(web_element)

    def clear_check_box(self, web_element):
        """
        Clears the given checkbox.

        :param web_element: Web element to clear the checkbox.
        """
        if web_element.is_selected():
            self.click_element_javascript(web_element)

    def is_element_displayed(self, by, locator):
        """
        Verifies if an element is displayed.

        :param by: The by element to find.
        :param locator: The locator of the element to find.
        :return: True if the WebElement is displayed, false otherwise.
        """
        try:
            return self.driver.find_element(by, locator).is_displayed()
        except StaleElementReferenceException:
            return self.is_element_displayed(by, locator)
        except NoSuchElementException:
            return False

    def wait_until_element_displayed(self, by=By):
        """
        Waits for an element is displayed.

        :param by: Element to wait.
        :return: True if the element is found, false otherwise.
        """
        try:
            self.wait.until(visibility_of_element_located(by))
            return True
        except TimeoutError:
            logger.info("Element not found")
            return False

    def switch_to_iframe(self, iframe):
        """
        Switches to the given iframe.

        :param iframe: iframe to switch.
        """
        self.driver.switch_to_frame(iframe)

    def switch_to_default(self):
        """
        Switches to the default content on the page.
        """
        self.driver.switch_to.default_content()

    def wait_for_clickable_element(self, by, time_to_wait=3):
        """
        Waits for an element to be clickable with default time of 3 secs.

        :param by: By locator to search and wait for the element.
        :param time_to_wait: Time in seconds to wait for the element.
        :return: Web Element ready to be clicked.
        """
        ignored_exceptions = (
            NoSuchElementException,
            StaleElementReferenceException,
        )
        return WebDriverWait(self.driver, time_to_wait, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.presence_of_element_located(by)
        )

    def scroll_to_bottom(self):
        """
        Scrolls to bottom of the page.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def get_element_value(self, web_element):
        """
        Waits and gets the text of a WebElement.

        :param web_element: WebElement to wait and get the text.
        :return: Text of the WebElement.
        """
        self.wait.until(visibility_of(web_element))
        return web_element.get_attribute(self.VALUE_ATTR)
