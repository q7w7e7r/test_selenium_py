from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    DESCRIPTION = (By.CSS_SELECTOR, "#product_description + p")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert-info > div > p:nth-child(1) > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
