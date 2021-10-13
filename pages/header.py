from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    CART_ICON = (By.ID, 'nav-cart-count')
    RETURN_ORDER_ICON = (By.CSS_SELECTOR, "div#nav-tools a[href*='order-history?ref_=nav_orders']")
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')

    def click_cart(self):
        self.click(*self.CART_ICON)

    def return_order(self):
        self.click(*self.RETURN_ORDER_ICON)

    def input_field(self,search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def search_click(self):
        self.click(*self.SEARCH_ICON)