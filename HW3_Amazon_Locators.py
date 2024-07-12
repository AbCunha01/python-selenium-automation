from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register')

# Amazon logo
driver.find_element(By.CSS_SELECTOR('[aria-label*="Amazon"]'))
# 'Create Account' Logo:
driver.find_element(By.CSS_SELECTOR("a-spacing-small"))
#Your Name:
driver.find_element(By.CSS_SELECTOR("ap_customer_name"))
#Mobile number or email:
driver.find_element(By.CSS_SELECTOR ("ap_email"))
#Password:
driver.find_element(By.CSS_SELECTOR("ap_password"))
#Password Must be at least 6 characters:
driver.find_element(By.CSS_SELECTOR("passwordHelp_ap_password"))
#Re-Enter Password:
driver.find_element(By.CSS_SELECTOR('input.ap_password_check'))
#Create Your Amazon Account:
driver.find_element(By.CSS_SELECTOR('input.auth-continue-announce'))
#Conditions of use:
driver.find_element(By.CSS_SELECTOR('a.Conditions of Use'))
#Privacy Notice:
driver.find_element(By.CSS_SELECTOR('a.Privacy Notice'))
#Already Have an Account?  Sign IN:
driver.find_element(By.CSS_SELECTOR('a.a-link-emphasis'))

driver.quit()