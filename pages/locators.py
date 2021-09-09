from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_SELECTOR = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM_SELECTOR = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-info")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    TEXT = (By.CSS_SELECTOR, "#content_inner p")
    ITEM_BASKET = (By.CSS_SELECTOR, ".basket-items")
