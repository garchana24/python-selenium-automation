from selenium.webdriver.common.by import By
from behave import given,when,then

PRODUCT_COLOR = (By.CSS_SELECTOR, "div#variation_color_name img.imgSwatch")
CURRENT_COLOR = (By.CSS_SELECTOR, "div#variation_color_name .selection")


@when('Select a bag item')
def select_item(context):
    #context.driver.find_element(By.CSS_SELECTOR, "img.s-image[alt*='Sponsored Ad - Amazon Basics Large Travel Luggage']").click()
    context.app.product_list.product_select()


@when('Add the item to cart')
def add_item(context):
    #context.driver.find_element(By.ID, 'add-to-cart-button').click()
    context.app.product_list.add_to_cart()


@given('Open Amazon product B081YS2F7N page')
def product_page(context):
    context.driver.get('https://www.amazon.com/dp/B081YS2F7N')


@then('Verify user clicks on the different colors')
def product_link(context):
    expected_colors = ['Black','Blue','Burgundy','Caramel','Gray','Green','Khaki']
    products = context.driver.find_elements(*PRODUCT_COLOR)
    for i in range(7):
        products[i].click()
        #print(products[i])
        current_color_link = context.driver.find_element(*CURRENT_COLOR).text
        #print(current_color_link)

        assert current_color_link == expected_colors[i], f'Error expected {expected_colors[i]} did not match {current_color_link}'

