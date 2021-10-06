from selenium.webdriver.common.by import By
from behave import given,when,then



BESTSELLER_LINKS = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a[href*='/gp']")

@when('Open Amazon Bestsellers page')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/')
    #context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify if there are {expected_link_count} number of links')
def bestseller_link_count(context, expected_link_count):
    link_results = context.driver.find_elements(*BESTSELLER_LINKS)
    print(link_results)
    actual_link_count = len(link_results)
    assert actual_link_count == int(expected_link_count), f'Error! , The Actual_result {actual_link_count} does not match the expected result {expected_link_count}'


@then('Verify page by clicking on the links in header')
def click_header_links(context):
    link_results = context.driver.find_elements(*BESTSELLER_LINKS)
    size = len(link_results)
    for i in range(size):
        link_results[i].click()
        current_page = context.driver.find_elements(By.XPATH, "//li/div //a[contains(@href, '/gp/')]")
        link_results = context.driver.find_elements(*BESTSELLER_LINKS)
        assert current_page[i].text == link_results[i].text, f'Actual page {current_page[i].text} is not same as {link_results[i].text}'







