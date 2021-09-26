from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given,when,then


@given('Open Amazon help page')
def open_amazonhelp(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_word} in search field')
def input_searchword(context,search_word):
    context.driver.find_element(By.ID, 'helpsearch').send_keys(search_word, Keys.ENTER)
