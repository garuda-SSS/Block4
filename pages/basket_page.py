from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_be_no_text()
        self.should_be_no_goods()

    def should_be_no_text(self):
        item=self.browser.find_element(*BasketPageLocators.TEXT_EMPTY)
        text=item.text
        assert "Your basket is empty" in text, "Message 'Your basket is empty' is missing"

    def should_be_no_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY),"Items is in basket"

        

        
