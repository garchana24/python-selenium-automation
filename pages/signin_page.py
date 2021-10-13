from pages.base_page import Page
from selenium.webdriver.common.by import By

class Signin(Page):
    SIGNIN_TEXT = (By.CSS_SELECTOR, "div.a-box h1.a-spacing-small")
    def check_signin_page(self,expected_text):
        self.verify_text(expected_text, *self.SIGNIN_TEXT)
