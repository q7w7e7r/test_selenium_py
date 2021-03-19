from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.is_element_present(*ProductPageLocators.CART)
        prod_name = self.get_product_name()
        self.browser.find_element(*ProductPageLocators.CART).click()
        self.solve_quiz_and_get_code()
        name_added_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADDET_TO_CART).text
        assert prod_name == name_added_product, \
            f"Name product addet to cart not correct, coorect name {prod_name}, name added {name_added_product}"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
