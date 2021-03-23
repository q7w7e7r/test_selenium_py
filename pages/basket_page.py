from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def cart_should_be_empty(self):
        assert not self.is_element_present(*BasketPageLocators.TITLE), \
            "There are products in the shopping cart"

    def cart_should_have_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Not found message 'empty basket'"
