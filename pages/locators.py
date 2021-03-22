from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    DESCRIPTION = (By.CSS_SELECTOR, "#product_description + p")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert-info > div > p:nth-child(1) > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LANGUAGE = (By.CSS_SELECTOR, "[name='language']")
    LANGUAGE_DE = (By.CSS_SELECTOR, 'option[value="de"]')
    CONFIRM_CHANGE_LANGUAGE = (By.CSS_SELECTOR, '#language_selector > button')
    BTN_FIND = (By.CSS_SELECTOR, 'input[ value="Search"]')
    FIND_TEXT = (By.CSS_SELECTOR, '#id_q')
    OSCAR = (By.CSS_SELECTOR, "[title = 'Oscar T-shirt']")
    BTN_VIEW_BASKET = (By.CSS_SELECTOR,".basket-mini a.btn")

class BasketPageLocators():
    TITLE =(By.CSS_SELECTOR, '#content_inner > .basket-title')
    EMPTY_MESSAGE =(By.CSS_SELECTOR, '#content_inner > p > a')