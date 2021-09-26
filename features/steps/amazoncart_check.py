from selenium.webdriver.common.by import By
from behave import given,when,then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-icon.nav-sprite").click()


@when('Enter bag into search field')
def input_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('bag')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

