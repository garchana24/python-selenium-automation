from selenium.webdriver.common.by import By
from behave import given,when,then


@then('Verify cart empty text is shown')
def verify_cart(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2").text
    expected_result = 'Your Amazon Cart is empty'
    assert actual_result == expected_result, f'Error! , The Actual_result {actual_result} does not match the expected result {expected_result}'


@then('Verify count in cart icon')
def verify_cartcount(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[contains(@class,'nav-cart-count nav-cart-1')]").text
    expected_result = '1'
    assert actual_result == expected_result, f'Error! , The Actual_result {actual_result} does not match the expected result {expected_result}'