from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    # Провека наличия кнопки "Добавить в корзину"
    def should_be_cart_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), \
            "Not found button add to cat"

    # Проверка наличия информации о товаре
    def should_be_product_info(self):
        assert self.is_element_present(*ProductPageLocators.DESCRIPTION), \
            "Not found product info"
    # Добавить в корзину
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    # Сравнение имени в alert с именем из описания продукта
    def check_added_product_name_with_alert(self):
        name_in_alert = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert name in name_in_alert, \
            f"Name product added to cart not correct, correct name {name}, name added {name_in_alert}"
    # Сравнение цены в описании товара с alert
    def check_price_pr_info_with_alert(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_alert = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price == price_alert, \
            f"Different price in info {price} and alert {price_alert}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def go_to_cart_page(self):
        button_basket = self.browser.find_element(*BasePageLocators.BTN_VIEW_BASKET)
        button_basket.click()


