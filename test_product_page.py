from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium import webdriver
import time
import pytest
import random


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page=LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password=str(random.randint(10000, 99999)) + "!Aa!"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207")
        page.open()
        page.should_not_be_success_message() 

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207")
        page.open()
        page.user_put_to_basket()
        page.should_be_after_add()     

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.put_to_basket()
    page.should_be_after_add()

    
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link): 
    page = ProductPage(browser, link)
    page.open()
    page.put_to_basket()
    page.should_not_be_success_message()

@pytest.mark.need_review    
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message(browser, link): 
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()   

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.put_to_basket()
    page.should_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()




    
