from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BTN_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
        price_elem = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        name_elem = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        price = self.text_elem(price_elem)
        name = self.text_elem(name_elem)
        self.check_name(name)
        self.check_price(price)

    def text_elem(self, elem):
        return elem.text

    def check_name(self, name):
        name_elem = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET)
        name_text = self.text_elem(name_elem)
        assert name_text == name, "The name is different"

    def check_price(self, price):
        price_elem = self.browser.find_element(*ProductPageLocators.PRICE_BUTTON)
        price_text = self.text_elem(price_elem)
        assert price_text == price, "The price is different"





