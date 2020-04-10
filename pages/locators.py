from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_from")
    REG_FORM = (By.CSS_SELECTOR, "#register_from")


class ProductPageLocators():
    BTN_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".price_color")
    PRICE_BUTTON = (By.CSS_SELECTOR, ".visible-xs-inline-block")
    NAME_PRODUCT = (By.XPATH,"//h1[text()='Coders at Work']")
    NAME_IN_BASKET = (By.XPATH,"//strong[text() = 'Coders at Work']")