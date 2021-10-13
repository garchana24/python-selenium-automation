from selenium.webdriver.common.by import By
from behave import given,when,then

@then('Verify if amazon sign in page opens')
def verify_signin_page(context):
    expected_result = 'Sign-In'
    context.app.signin_page.check_signin_page(expected_result)
