from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT), "No text"

    def should_be_is_empty(self):
        assert self.is_disappeared(*BasketPageLocators.ITEM_BASKET), "Basket must be empty"
