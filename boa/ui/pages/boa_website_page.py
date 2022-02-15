from selenium.webdriver.support.expected_conditions import visibility_of

from boa.ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


import re

from utils.date_helper import DateHelper


class BoaWebsitePage(BasePage):
    __BOOK_FLIGHTS_MENU_CSS = "li[class='menu selected']"
    __FROM_LST_ID = "select_desde"
    __TO_LST_ID = "select_hasta"
    __ROUND_TRIP_BTN_ID = "rbtn_ida_vuelta"
    __ONE_WAY_BTN_ID = "rbtn_ida"
    __DEPARTURE_TXT_BOX_ID = "picker_salida"
    __RETURN_TXT_BOX_ID = "picker_regreso"
    __ADULTS_SELECT_ID = "select_nro_adultos"
    __CHILD_SELECT_ID = "select_nro_ninhos"
    __INFANTS_SELECT_ID = "select_nro_bebes"
    __SEARCH_BTN_ID = "btn_buscar_vuelos"

    __CALENDAR_LINK_XPATH = "//td[@data-month='{0}']//a[text()='{1}']"
    __NEXT_BTN_CSS = "a[class*='next ui-corner-all']"

    def wait_until_page_object_is_loaded(self):
        self.wait.until(visibility_of(self.driver.find_element(By.CSS_SELECTOR, self.__BOOK_FLIGHTS_MENU_CSS)))

    def __set_date(self, date):
        new_date = re.search(r"(\d.)\/(\d.)\/(\d.*)", date)
        day = int(new_date.group(1))
        month = int(new_date.group(2)) - 1
        calendar_link_xpath = self.__CALENDAR_LINK_XPATH.format(str(month), str(day))
        while True:
            if self.driver_tool.is_element_displayed(By.XPATH, calendar_link_xpath):
                self.driver_tool.click_element(self.driver.find_element(By.XPATH, calendar_link_xpath))
                break
            else:
                self.driver_tool.click_element(self.driver.find_element(By.CSS_SELECTOR, self.__NEXT_BTN_CSS))

    def __select_from_lst(self, place):
        self.driver_tool.select_lst_box_option(self.driver.find_element(By.ID, self.__FROM_LST_ID), place)

    def __select_to_lst(self, place):
        self.driver_tool.select_lst_box_option(self.driver.find_element(By.ID, self.__TO_LST_ID), place)

    def __select_way_lst(self, way):
        if way == 'one-way':
            self.driver_tool.click_element(self.driver.find_element(By.ID, self.__ONE_WAY_BTN_ID))
        elif way == 'round-trip':
            self.driver_tool.click_element(self.driver.find_element(By.ID, self.__ROUND_TRIP_BTN_ID))

    def __set_departure_txt_box(self, date):
        new_date = DateHelper.convert_date(date)
        self.driver_tool.click_element(self.driver.find_element(By.ID, self.__DEPARTURE_TXT_BOX_ID))
        self.__set_date(new_date.strftime("%d/%m/%Y"))

    def __set_return_txt_box(self, date):
        new_date = DateHelper.convert_date(date)
        self.driver_tool.click_element(self.driver.find_element(By.ID, self.__RETURN_TXT_BOX_ID))
        self.__set_date(new_date.strftime("%d/%m/%Y"))

    def __select_adults(self, quantity):
        self.driver_tool.select_lst_box_option(self.driver.find_element(By.ID, self.__ADULTS_SELECT_ID), quantity)

    def __select_child(self, quantity):
        self.driver_tool.select_lst_box_option(self.driver.find_element(By.ID, self.__CHILD_SELECT_ID), quantity)

    def __select_infant(self, quantity):
        self.driver_tool.select_lst_box_option(self.driver.find_element(By.ID, self.__INFANTS_SELECT_ID), quantity)

    def __compose_boa_website_dict(self):
        strategy_map = {
            "from_location": self.__select_from_lst,
            "to_location": self.__select_to_lst,
            "select": self.__select_way_lst,
            "departure_date": self.__set_departure_txt_box,
            "return_date": self.__set_return_txt_box,
            "adults": self.__select_adults,
            "child": self.__select_child,
            "infant": self.__select_infant
        }
        return strategy_map

    def _process_book_flight_information(self, data_dict):
        book_flight_data = {}
        for row in data_dict:
            book_flight_data[row["Field"]] = row["Value"]

        strategy_methods = self.__compose_boa_website_dict()

        for key in book_flight_data:
            method = strategy_methods[key].__get__(self, type(self))
            method(book_flight_data.get(key))

    def search_book_flight_information(self, data_dict):
        self.driver_tool.click_element(self.driver.find_element(By.CSS_SELECTOR, self.__BOOK_FLIGHTS_MENU_CSS))
        self._process_book_flight_information(data_dict)
        self.driver_tool.click_element(self.driver.find_element(By.ID, self.__SEARCH_BTN_ID))
