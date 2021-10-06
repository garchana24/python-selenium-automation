from selenium.webdriver.common.by import By
from behave import given,when,then
from selenium.webdriver.support import expected_conditions as EC


@given('Open Amazon T&C page')
def open_amazon_TC_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_orig_window(context):
    context.orig_window = context.driver.current_window_handle
    print(context.orig_window)


@when('Click on Amazon Privacy Notice link')
def click_Privacy_Notice(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href,'https://www.amazon.com/privacy')]").click()
    context.driver.wait.until(EC.new_window_is_opened)