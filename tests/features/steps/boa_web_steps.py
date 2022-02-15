import logging

from boa.entity.book_flight import BookFlight
from boa.ui.pages.find_flight_page import FindFlight

logger = logging.getLogger(__name__)

from behave import given
from behave import when
from behave import then

from behave import use_step_matcher
from boa.ui.page_transporter import PageTransporter
from boa.ui.pages.boa_website_page import BoaWebsitePage
logger = logging.getLogger(__name__)


use_step_matcher("re")


@given(u'I navigate to BOA website')
def navigate_to_boa_website_page(context):
    logger.info('I navigate to Dashboard page')
    PageTransporter(context.web_driver_manager).navigate_to_boa()


@when(u'I set in the Book Flight tab the following data')
def set_in_the_book_flight_tab(context):
    logger.info('I navigate to Dashboard page')
    context.boa_website = BoaWebsitePage(context.web_driver_manager)
    context.boa_website.search_book_flight_information(context.table)
    context.book_flight = BookFlight()
    context.book_flight.process_book_flight_information(context.table)


@then('the "(.*?)" should be the same as the Book Flight searching')
def verify_date_are_same_as_book_flight(context, field):
    find_flight_page = FindFlight(context.web_driver_manager)
    if "departure" in field:
        logger.info("Testing departure date")
        assert find_flight_page.is_date_displayed(context.book_flight.get_book_flight_field("departure_date")), (
            "the " + context.book_flight.get_book_flight_field("departure_date").strftime("%d/%m/%Y")
            + " is not displayed in the Find FLight page"
        )
    if "return" in field:
        logger.info("Testing return date")
        assert find_flight_page.is_date_displayed(context.book_flight.get_book_flight_field("return_date")), (
            "the " + context.book_flight.get_book_flight_field("return_date").strftime("%d/%m/%Y")
            + " is not displayed in the Find FLight page"
        )
    if "from" in field or "to" in field:
        logger.info("Testing from and to location")
        assert context.book_flight.get_book_flight_field("from_location") in find_flight_page.get_location().upper(), (
                "the " + context.book_flight.get_book_flight_field("from_location")
                + " is not displayed in the Find FLight page"
        )
        assert context.book_flight.get_book_flight_field("to_location") in find_flight_page.get_location().upper(), (
                "the " + context.book_flight.get_book_flight_field("to_location")
                + " is not displayed in the Find FLight page"
        )
    if "adults" in field:
        logger.info("Testing adults quantity")
        assert context.book_flight.get_book_flight_field("adults") in find_flight_page.get_adults(), (
                "the " + context.book_flight.get_book_flight_field("adults")
                + " is not displayed in the Find FLight page"
        )