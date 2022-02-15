from abc import ABC, abstractmethod


class IDriver(ABC):
    """
    Initialize the Selenium web driver.
    """

    @abstractmethod
    def init_driver(self):
        """
        Initialize web driver.

        :return: Instance of Driver.
        """
