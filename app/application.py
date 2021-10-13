from pages.main_page import MainPage
from pages.header import Header
from pages.cart_verify_page import CartVerify
from pages.signin_page import Signin
from pages.product_list import Products


class Application:
    def __init__(self,driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.cart_verify = CartVerify(self.driver)
        self.signin_page = Signin(self.driver)
        self.product_list = Products(self.driver)
