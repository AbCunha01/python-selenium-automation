from behave import given, when, then
from selenium.webdriver.common.by import By

@given('user is on the Target homepage')
def step_impl(context):
    context.driver.get("https://www.target.com/")

@when('user searches for "{product}"')
def search_product(context, product):
    context.driver.find_element(By.ID, "search").send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('search results should contain "{product}')
def step_impl(context, product):
    product_titles = context.browser.find_elements(By.CSS_SELECTOR, ".product-title")
    assert any(product_title.text.lower() == product.lower() for product_title in product_titles)

@given('user is on the Target Circle page')
def step_impl(context):
    context.browser.get("https://www.target.com/circle")

@when('user verifies benefit cells')
def step_impl(context):
    context.benefit_cells = context.browser.find_elements(By.CSS_SELECTOR, ".circle-benefit-cell")

@then('there should be at least 10 benefit cells')
def step_impl(context):
    assert len(context.benefit_cells) >= 10

@given('Open Target main page')
def step_impl(context):
    context.browser.get("https://www.target.com/")

@when('Search for "{product_name}"')
def step_impl(context, product):
    search_box = context.browser.find_element(By.ID, "search")
    search_box.send_keys(product)
    search_button = context.browser.find_element(By.ID, "Search")
    search_button.click()

@when('Click on Add to Cart button')
def step_impl(context):
    add_to_cart_button = context.browser.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']")
    add_to_cart_button.click()
    sleep(2)

@when('Confirm Add to Cart button from side navigation')
def step_impl(context):
    # This assumes a confirmation message or button appears in the side navigation.
    # You may need to adjust the locator accordingly.
    confirm_button = context.browser.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='Add to cart']")
    confirm_button.click()
    sleep(4)

@when('Open Cart page')
def verify_cart_items(context, ammount, cart_icon=None):
    cart_summary = context.diver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal']")
    cart_icon.click()
    assert f'{ammount} item' if cart_summary else f"Expected {ammount} items but got {cart_summary}"


@then('Verify cart has 1 item(s)')
def step_impl(context):
    cart_item_count = context.browser.find_element(By.CSS_SELECTOR, "*/icons/Cart.svg#Cart")
    assert cart_count.text == "1"

    driver.quit()