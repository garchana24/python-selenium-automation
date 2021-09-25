from selenium.webdriver.common.by import By
from behave import given,when,then

@when('Select a bag item')
def select_item(context):
    context.driver.find_element(By.CSS_SELECTOR, "img.s-image[src='https://m.media-amazon.com/images/I/61bSEhAEHnL._AC_UL320_.jpg']").click()

@when('Add the item to cart')
def add_item(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()