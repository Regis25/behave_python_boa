from selenium.webdriver.support.expected_conditions import visibility_of

from boa.ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FindFlight(BasePage):
    __MODIFY_SEARCH_BTN_ID = "btn_cambiar_vuelo"
    __DATE_DEPARTURE_RETURN_LBL_XPATH = "//td[@class='day-selector selected' and ./span[text()='{day}']]" \
                                        "//h2[text()='{month}']//span[text()='{date}']"
    __LOCATIONS_LBL_XPATH = "//*[@id='info_resultados_vuelos']/div/b"
    __QUANTITY_ADULTS_LBL_XPATH = "//*[@id='tabla_tipo']/tbody/tr[2]/td[2]"

    def wait_until_page_object_is_loaded(self):
        self.wait.until(visibility_of(self.driver.find_element(By.ID, self.__MODIFY_SEARCH_BTN_ID)))

    def is_date_displayed(self, date):
        date_lbl_xpath = self.__DATE_DEPARTURE_RETURN_LBL_XPATH.format(day=date.strftime("%A"),
                                                                       month=date.strftime("%b"),
                                                                       date=date.strftime("%d"))
        return self.driver_tool.is_element_displayed(By.XPATH, date_lbl_xpath)

    def get_location(self):
        return self.driver_tool.get_element_text(self.driver.find_element(By.XPATH, self.__LOCATIONS_LBL_XPATH))

    def get_adults(self):
        return self.driver_tool.get_element_text(self.driver.find_element(By.XPATH, self.__QUANTITY_ADULTS_LBL_XPATH))
