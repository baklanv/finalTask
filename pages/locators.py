from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_SELECTOR = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM_SELECTOR = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-info")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")


class BasketPageLocators():
    TEXT = (By.CSS_SELECTOR, "#content_inner p")
    ITEM_BASKET = (By.CSS_SELECTOR, ".basket-items")
