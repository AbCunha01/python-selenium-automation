from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# Amazon logo
driver.find_element(By.XPATH,'//*[@class="a-link-nav-icon"]')
# Email field
driver.find_element(By.XPATH,'//input[@type="email"]')
# Continue button
driver.find_element(By.ID, 'continue')
# Conditions of use link
driver.find_element(By.ID,'Conditions of Use')
# Privacy Notice link
driver.find_element(By.ID,'Privacy Notice')
# Need help link
driver.find_element(By.XPATH,'//*[@class="a-expander-prompt"]')
# Forgot your password link
driver.find_element(By.ID,'Forgot your password?')
# Other issues with Sign-In link
driver.find_element(By.ID,'Other issues with Sign-In')
# Create your Amazon account button
driver.find_element(By.ID,'createAccountSubmit')

driver.quit()

