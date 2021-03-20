from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    # Провека наличия кнопки "Добавить в корзину"
    def should_be_link_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.CART), \
            "Not found button add to cat"
    # Проверка наличия информации о товаре
    def should_be_product_info(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), \
            "Not found product info"
    # Добавить в корзину
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.CART).click()
        # self.solve_quiz_and_get_code()
        self.check_added_product_name_with_alert()
    # Проверка имени в alert добавленного продукта с именем из описания продукта
    def check_added_product_name_with_alert(self):
        name_added_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADDET_TO_CART).text
        prod_name = self.get_product_name()
        assert prod_name == name_added_product, \
            f"Name product added to cart not correct, correct name {prod_name}, name added {name_added_product}"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
