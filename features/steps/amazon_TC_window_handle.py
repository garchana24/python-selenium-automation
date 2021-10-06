from selenium.webdriver.common.by import By
from behave import given,when,then
from selenium.webdriver.support import expected_conditions as EC


@when('Switch to the newly opened window')
def switch_new_window(context):
    all_window_handles = context.driver.window_handles
    print(all_window_handles)
    context.driver.switch_to.window(all_window_handles[1])
    print(context.driver.current_window_handle)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacynotice_page(context):
    expected_context = 'Amazon.com Privacy Notice'
    actual_context = context.driver.find_element(By.CSS_SELECTOR, "div.help-content h1").text
    print(actual_context)
    assert actual_context == expected_context, f'In the wrong page {actual_context} , have to be in page {expected_context}'


@then('User can close new window')
def closenew_restore_orig_window(context):
        all_window_handles = context.driver.window_handles
        print(all_window_handles)
        print(f'Current active window:',{context.driver.current_window_handle})
        context.driver.close()
        #print(f'Current active window after close action:', {context.driver.current_window_handle})
        print(all_window_handles)


@then('Switch back to original')
def switch_original_window(context):
    context.driver.switch_to.window(context.orig_window)
    print(context.driver.current_window_handle)
    


