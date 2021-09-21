from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

#Amazon logo(Parent Child- 2 level up)
driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-medium a-text-center']//i[@class='a-icon a-icon-logo']")

#Email field(Parent and child- 1 level)
driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@type='email']")

#Continue Button
driver.find_element(By.ID, 'continue')

#Need help link(Using * for tagname)
driver.find_element(By.XPATH, "//*[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.XPATH, "//a[contains(text() ,'Forgot your password')]")

#Other issues with Sign-In link(multiple attributes)
driver.find_element(By.XPATH, "//*[@class='a-link-normal' and @id='ap-other-signin-issues-link']")

#Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit' and @class='a-button-text']")

#Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'/gp/help/customer/display.html/ref=ap_signin_notification_condition')]")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href,'/gp/help/customer/display.html/ref=ap_signin_notification') and text()='Privacy Notice']")
