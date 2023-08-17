from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def put_to_basket(self):
        basket=self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket.click()
        self.solve_quiz_and_get_code()

    def should_be_after_add(self):
        self.should_be_right_name()
        self.should_be_right_cost()
    
    def should_be_right_name(self):
        name1=self.browser.find_element(*BasketPageLocators.NAME_IN_PAGE)
        text1=name1.text
        name2=self.browser.find_element(*BasketPageLocators.NAME_IN_BASKET)
        text2=name2.text
        
        print(f"{text1} и {text2}")
        
        assert text1==text2, "Wrong book is in basket"

    def should_be_right_cost(self):
        price1=self.browser.find_element(*BasketPageLocators.PRICE_IN_PAGE)
        cost1=price1.text

        price2=self.browser.find_element(*BasketPageLocators.PRICE_IN_BASKET)
        cost2=price1.text
        
        print(f"{cost1} и {cost2}")
        assert cost1==cost2, "Wrong price is in basket"
