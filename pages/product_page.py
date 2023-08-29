from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def put_to_basket(self):
        basket=self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
        self.solve_quiz_and_get_code()
        
    def user_put_to_basket(self):
        basket=self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()

    def should_be_after_add(self):
        self.should_be_right_name()
        self.should_be_right_cost()
    
    def should_be_right_name(self):
        name1=self.browser.find_element(*ProductPageLocators.NAME_IN_PAGE)
        text1=name1.text
        name2=self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET)
        text2=name2.text
        assert text1==text2, "Wrong book is in basket"

    def should_be_right_cost(self):
        price1=self.browser.find_element(*ProductPageLocators.PRICE_IN_PAGE)
        cost1=price1.text
        price2=self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        cost2=price1.text
        assert cost1==cost2, "Wrong price is in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should be hide"
