from pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):

    CART_CHECK_TEXT = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2")
    CART_PROD_TEXT = (By.CSS_SELECTOR, "span.a-truncate-cut")
    CART_COUNT = (By.XPATH, "//span[contains(@class,'nav-cart-count nav-cart-1')]")

    def verify_cart_check(self,expected_text):
        self.verify_text(expected_text, *self.CART_CHECK_TEXT)

    def verify_cart_count(self,expected_count):
        self.verify_text(expected_count,*self.CART_COUNT)

    def verify_cart_prod_name(self,expected_text):
        self.verify_text(expected_text,*self.CART_PROD_TEXT)
