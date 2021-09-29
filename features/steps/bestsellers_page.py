from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given,when,then
from time import sleep

BESTSELLER_LINKS = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a[href*='/gp']")

@when('Open Amazon Bestsellers page')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/')
    #context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify if there are {expected_link_count} number of links')
def bestseller_link_count(context, expected_link_count):
    link_result = context.driver.find_elements(*BESTSELLER_LINKS)
    print(link_result)
    actual_link_count = len(link_result)
    assert actual_link_count == int(expected_link_count), f'Error! , The Actual_result {actual_link_count} does not match the expected result {expected_link_count}'

