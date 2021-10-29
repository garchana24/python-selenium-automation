from pages.main_page import MainPage
from pages.header import Header
from pages.cart import Cart
from pages.signin_page import Signin
from pages.product_list import Products
from pages.base_page import Page


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.cart = Cart(self.driver)
        self.signin_page = Signin(self.driver)
        self.product_list = Products(self.driver)
        self.base_page = Page(self.driver)
