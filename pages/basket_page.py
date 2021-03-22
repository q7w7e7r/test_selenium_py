from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasketPageLocators
import math

class BasketPage(BasePage):
    def check_empty_product(self):
        assert not self.is_element_present(*BasketPageLocators.TITLE), \
            "There are products in the shopping cart"
    def check_message_empty(self):
        assert  self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Not found message 'empty basket'"