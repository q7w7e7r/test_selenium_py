import math
import time

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        # Баг - елси запустить все тесты в каталоге то получаю ошибку в Chrome:
        # def should_be_authorized_user(self):
        # > assert self.is_element_present(*BasePageLocators.USER_ICON), \
        #     "User icon is not presented, probably unauthorised user"
        # E
        # AssertionError: User icon is not presented, probably unauthorised user
        # Если запустить тесты класса TestUserAddToBasketFromProductPage отдельно то ошибки нету
        # с помощью задержки на секунду баг был исправлен
        time.sleep(1)
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def change_language_on_de(self):
        self.browser.find_element(*BasePageLocators.LANGUAGE_DE).click()
        self.browser.find_element(*BasePageLocators.CONFIRM_CHANGE_LANGUAGE).click()

    def check_current_language(self, lang):
        if f"{lang}" in self.browser.find_element(*BasePageLocators.LANGUAGE_DE).text:
            return True
        else:
            return False

    def find(self, something):
        self.browser.find_element(*BasePageLocators.FIND_TEXT).send_keys(f"{something}")
        self.browser.find_element(*BasePageLocators.BTN_FIND).click()
        return self.is_element_present(*BasePageLocators.OSCAR)

    def open_basket(self):
        self.browser.find_element(*BasePageLocators.BTN_VIEW_BASKET).click()

    def should_be_authorized_user(self):
        # Баг - если запустить все тесты в каталоге то иконка на одном из тестов не успевает отрисоваться
        # с помощью проверки баг был исправлен
        self.is_element_present(*BasePageLocators.USER_ICON)
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
