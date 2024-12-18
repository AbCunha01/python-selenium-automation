from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


#Feature: Verify Empty Cart Message
@given("I am on the Target homepage")
def open_main(context):
    context.driver.get('https://www.target.com/')


    @when("I click the cart icon")
    def click_cart_icon(context):
        cart_icon = context.driver.find_element(By.CSS_SELECTOR('Cart.svg#Cart')).click()


    @then("Verify the 'Your cart is empty' message")
    def verify_empty_cart_message(context):
        empty_message = context.driver.find_element(By.CSS_SELECTOR("Your cart is empty")).text
        assert empty_message == "Your cart is empty"


# Update these steps
def click_cart_icon(context):
  cart_icon = context.driver.find_element(By.CSS_SELECTOR('Cart.svg#Cart')).click()

@When("I click 'Sign In' from the navigation menu")
def click_sign_in_nav(context):
    sign_in_link = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title='Sign in']"))
    )
    sign_in_link.click()

@Then("Verify that the 'Sign In' form opened")
def verify_sign_in_form(context):
  sign_in_form = context.driver.find_element(By.ID("Sign in"))
  assert sign_in_form.is_displayed()
