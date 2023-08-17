from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_IN_PAGE= (By.CSS_SELECTOR, ".product_main h1")
    NAME_IN_BASKET= (By.CSS_SELECTOR, ".product_main h1:first-child")
    PRICE_IN_PAGE= (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_BASKET= (By.CSS_SELECTOR, ".alertinner p strong")
