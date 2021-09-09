from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def addToBasket(self):
        button = self.browser.find_element(*ProductPageLocator.ADD_BASKET)
        button.click()

    def should_be_add_product(self):
        self.the_price_matches(self.get_selector_product("div.col-sm-6.product_main .price_color"))
        self.name_matches(self.get_selector_product("div h1"))

    def the_price_matches(self, name):
        selector = "//strong[text()=\"" + name + "\"]"
        print(selector)
        assert self.is_element_present(By.XPATH, selector), "Wrong product name"

    def name_matches(self, price):
        assert self.is_element_present(By.XPATH, "//strong[text()=\"" + price + "\"]"), "Wrong product price"
