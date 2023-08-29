from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL= (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD= (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD= (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON= (By.NAME, "registration_submit")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_IN_PAGE= (By.CSS_SELECTOR, ".product_main h1")
    NAME_IN_BASKET= (By.CSS_SELECTOR, ".alertinner strong:first-child")
    PRICE_IN_PAGE= (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_BASKET= (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child")
    
class BasketPageLocators():
    OPEN_BASKET = (By.CSS_SELECTOR, "[href*=basket]:first-child")
    TEXT_EMPTY=(By.CSS_SELECTOR, "#content_inner")
    ITEMS_TO_BUY=(By.CSS_SELECTOR, ".basket-title")
