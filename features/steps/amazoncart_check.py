from selenium.webdriver.common.by import By
from behave import given,when,then


@when('Click on cart icon')
def click_cart_icon(context):
    #context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-icon.nav-sprite").click()
    context.app.header.click_cart()


@when('Enter {search_word} into search field')
def input_product(context,search_word):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('bag')
    #context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.header.input_field(search_word)

@when('Click on amazon search icon')
def click_search(context):
    context.app.header.search_click()



