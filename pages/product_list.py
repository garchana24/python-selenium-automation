from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Products(Page):

    SELECT_ITEM = (By.CSS_SELECTOR, "img.s-image[alt*='Sponsored Ad - Amazon Basics Large Travel Luggage']")
    ADD_CART_BUTTON = (By.ID, 'add-to-cart-button')
    ELECTRONICS = (By.CSS_SELECTOR, "#nav-subnav[data-category='electronics']")
    DEPARTMENT = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")
    NEW_ARRIVALS = (By.XPATH, "//span[contains(text(),'New Arrivals')]")
    #NEW_ARRIVALS_DEALS = (By.CSS_SELECTOR, "div.mm-column a[href*='/s?i=fashion']")
    NEW_ARRIVALS_WOMEN = (By.XPATH, "//img[contains(@src,'Holiday_subnav_NA_Women.jpg')]")
    NEW_ARRIVALS_MEN = (By.XPATH, "//img[contains(@src,'Holiday_subnav_NA_Mens.jpg')]")
    NEW_ARRIVALS_GIRLS = (By.XPATH, "//img[contains(@src,'Holiday_subnav_NA_Girls.jpg')]")
    NEW_ARRIVALS_BOYS = (By.XPATH, "//img[contains(@src,'Holiday_subnav_NA_Boys.jpg')]")
    NEW_ARRIVALS_BABY = (By.XPATH, "//img[contains(@src,'Holiday_subnav_Baby.jpg')]")
    NEW_ARRIVALS_LUGGAGE = (By.XPATH, "//img[contains(@src,'subnav/NA_L.jpg')]")



    def _get_expected_category(self, expected_category):
        return [self.DEPARTMENT[0], self.DEPARTMENT[1].replace('{CATEGORY}', expected_category)]

    def product_select(self):
        self.wait_for_element_click(*self.SELECT_ITEM)

    def add_to_cart(self):
        self.wait_for_element_click(*self.ADD_CART_BUTTON)

    def verify_correct_dept(self, expected_dept: str):
        locator = self._get_expected_category(expected_dept)
        self.find_element(*locator)

    def hover_over_newarrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()
        sleep(2)

    def verify_newarrivals_deals(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS_WOMEN)
        self.find_element(*self.NEW_ARRIVALS_MEN)
        self.find_element(*self.NEW_ARRIVALS_GIRLS)
        self.find_element(*self.NEW_ARRIVALS_BOYS)
        self.find_element(*self.NEW_ARRIVALS_BABY)
        self.find_element(*self.NEW_ARRIVALS_LUGGAGE)



