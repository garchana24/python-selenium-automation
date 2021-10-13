from selenium.webdriver.common.by import By
from behave import given,when,then

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Click on Return&Orders link')
def returnorder_click(context):
    #context.driver.find_element(By.CSS_SELECTOR, "div#nav-tools a[href*='order-history?ref_=nav_orders']").click()
    context.app.header.return_order()
