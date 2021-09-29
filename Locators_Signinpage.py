from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

#Amazon logo(Css by class)
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

#Create Account(Css by class)
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#Name field(Css by ID)
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')

#Email_field(Css by ID)
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

#Password_field(Css by ID)
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')

#Password info(XPath)
driver.find_element(By.XPATH, "//div[contains(@class,'a-box a-alert-inline a-alert-inline-info')]")
#By CSS(Parent child with generic tag)
driver.find_element(By.CSS_SELECTOR, ".auth-inlined-information-message .a-alert-content")

#Re-enter password_field(Css by ID)
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')

#Create Button(ID)
driver.find_element(By.ID, 'continue')

#Conditions_of_Use(Css by partial attribute)
#driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition']")

#Privacy Notice(Css by partial attribute)
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy']")

#Sign-In(Css by Parent child node)
driver.find_element(By.CSS_SELECTOR, "div.a-row a[href*='/ap/signin?openid.pape.max_auth_age=0&openid.return_to']")

