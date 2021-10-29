from selenium.webdriver.common.by import By
from behave import given,when,then


@then('Verify cart empty text is shown')
def verify_cart(context):
    #actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2").text
    expected_text = 'Your Amazon Cart is empty'
    #assert actual_result == expected_result, f'Error! , The Actual_result {actual_result} does not match the expected result {expected_result}'
    context.app.cart.verify_cart_check(expected_text)


@then('Verify count is {expected_count} in cart icon')
def verify_cartcount(context,expected_count):
    #actual_result = context.driver.find_element(By.XPATH, "//span[contains(@class,'nav-cart-count nav-cart-1')]").text
    #expected_result = '1'
    #assert actual_result == expected_result, f'Error! , The Actual_result {actual_result} does not match the expected result {expected_result}'
    context.app.cart.verify_cart_count(expected_count)


@then('Verify if added product is same in cart')
def verify_cart_text(context):
    context.app.header.click_cart()
    #actual_text = context.driver.find_element(By.CSS_SELECTOR, "span.a-truncate-cut").text
    expected_text = 'Amazon Basics Large Travel Luggage Duffel Bag, Black'
    #assert actual_text == expected_text,f'Error!!'
    context.app.cart.verify_cart_prod_name(expected_text)