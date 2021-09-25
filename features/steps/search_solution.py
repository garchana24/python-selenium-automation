from selenium.webdriver.common.by import By
from behave import given,when,then


@then('Verify Cancel order text is shown')
def verify_results_text(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_result = 'Cancel Items or Orders'
    assert actual_result == expected_result, f'Error! , The Actual_result {actual_result} does not match the expected result {expected_result}'

