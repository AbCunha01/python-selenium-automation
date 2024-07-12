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

# Open the Target homepage
driver.get("https://www.target.com/")

def verify_empty_cart_message(driver):
    """
    This function verifies the "Your cart is empty" message on Target's homepage.

    Args:
        driver (webdriver): The Selenium WebDriver instance.
    """

    cart_icon_locator = By.ID  # Replace with the actual ID if it exists
    if not driver.find_element(cart_icon_locator):
        # If ID is not available, use alternative locators
        cart_icon_locator = By.CLASS_NAME  # Replace with appropriate class name(s)
        if not driver.find_element(cart_icon_locator):
            # If class name is not suitable, use XPath or CSS selector
            cart_icon_locator = By.XPATH  # Replace with appropriate XPath expression
            # or
            cart_icon_locator = By.CSS_SELECTOR  # Replace with appropriate CSS selector

    driver.find_element(cart_icon_locator).click()

    empty_cart_message_locator = By.XPATH  # Replace with appropriate XPath expression targeting the message element
    # or
    empty_cart_message_locator = By.CSS_SELECTOR  # Replace with appropriate CSS selector targeting the message element

    # Wait for the message to be displayed (adjust wait time as needed)
    sleep(2)
    assert driver.find_element(empty_cart_message_locator).is_displayed(), "Empty cart message not found!"


def verify_sign_in_navigation(driver):
    """
    This function verifies a logged-out user can navigate to the Sign In form.

    Args:
        driver (webdriver): The Selenium WebDriver instance.
    """

    # High-priority locator (if applicable)
    sign_in_button_locator = By.ID  # Replace with the actual ID of the Sign In button if it exists
    if not driver.find_element(sign_in_button_locator):
        # If ID is not available, use alternative locators
        sign_in_button_locator = By.CLASS_NAME  # Replace with appropriate class name(s)
        if not driver.find_element(sign_in_button_locator):
            # If class name is not suitable, use XPath or CSS selector
            sign_in_button_locator = By.XPATH  # Replace with appropriate XPath expression targeting the Sign In button
            # or
            sign_in_button_locator = By.CSS_SELECTOR  # Replace with appropriate CSS selector targeting the Sign In button

    driver.find_element(sign_in_button_locator).click()

    # Verify Sign In form title/header (replace with appropriate locator)
    sign_in_form_locator = By.XPATH  # Replace with XPath targeting the Sign In form title/header
    # or
    sign_in_form_locator = By.CSS_SELECTOR  # Replace with CSS selector targeting the Sign In form title/header


    sleep(2)
    assert driver.find_element(sign_in_form_locator).is_displayed(), "Sign In form not found!"


verify_empty_cart_message(driver)
verify_sign_in_navigation(driver)


driver.quit()