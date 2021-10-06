from selenium.webdriver.common.by import By
from behave import given,when,then


WHOLEFOODS_PRODUCTS = (By.XPATH, "//li[@class='s-result-item' and .//span[contains(@class,'regular-price')]]/div")


@given('Open Amazon Wholefoodsdeals page')
def open_wholefoodsdeals(context):
    context.driver.get('https://www.amazon.com/fmc/storedeals/?_encoding=UTF8&almBrandId=VUZHIFdob2xlIEZvb2Rz')

@when('Click on all Wholefoodsdeals products')
def get_products(context):
    wproducts = context.driver.find_elements(*WHOLEFOODS_PRODUCTS)
    for prod in wproducts:
        prod.click()

@then('Verify product names of the products')
def verify_wholesale_product(context):
    wproducts = context.driver.find_elements(*WHOLEFOODS_PRODUCTS)
    for wproduct in wproducts:
        #print(wproduct.text)
        assert 'Regular' in wproduct.text, f'Expected phrase Regular is not there'
        current_product = wproduct.find_element(By.CSS_SELECTOR,"span.a-size-medium.wfm-sales-item-card__product-name.a-text-bold").text
        print("Product name:",f'{current_product}')
        assert current_product, f'Non-empty product names'

