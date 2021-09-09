from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def addToBasket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button.click()

    def should_be_add_product(self):
        self.the_price_matches(self.get_selector_product("div.col-sm-6.product_main .price_color"))
        self.name_matches(self.get_selector_product("div h1"))

    def the_price_matches(self, name):
        assert self.is_element_present(By.XPATH, "//strong[text()=\"" + name + "\"]"), "Wrong product name"

    def name_matches(self, price):
        assert self.is_element_present(By.XPATH, "//strong[text()=\"" + price + "\"]"), "Wrong product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"