from pages.base_page import Page
from selenium.webdriver.common.by import By

class Products(Page):

    SELECT_ITEM = (By.CSS_SELECTOR, "img.s-image[alt*='Sponsored Ad - Amazon Basics Large Travel Luggage']")
    ADD_CART_BUTTON = (By.ID, 'add-to-cart-button')


    def product_select(self):
        self.wait_for_element_click(*self.SELECT_ITEM)

    def add_to_cart(self):
        self.wait_for_element_click(*self.ADD_CART_BUTTON)

