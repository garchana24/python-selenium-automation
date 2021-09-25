from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome()
driver.get('https://www.amazon.com/gp/help/customer/display.html')

#driver.find_element(By.XPATH, "//span[@class='a-size-medium a-text-bold']")
#driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order', Keys.ENTER)
search_box = driver.find_element(By.ID, 'helpsearch')
search_box.send_keys('Cancel Order')
search_box.send_keys(Keys.ENTER)

#Assertion
actual_result = driver.find_element(By.XPATH,"//div[@class='help-content']/h1").text
#actual_result = driver.find_element(By.XPATH,"//b[text()='Cancel Order']").text
expected_result = 'Cancel Items or Orders'

if actual_result == expected_result:
    print('Test Passed')
else:
    print('Test Failed')

assert actual_result == expected_result, f'Error! , The Actual_result {actual_result} does not match the expected result {expected_result}'

driver.quit()
