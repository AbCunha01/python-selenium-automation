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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Damazon%2Busa%2Bshop%26hvadid%3D685750085434%26hvdev%3Dc%26hvlocphy%3D9010687%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D4653006753302775073%26hvtargid%3Dkwd-300129314550%26hydadcr%3D7694_13589738%26tag%3Dgooghydr-20%26ref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Amazon logo
driver.find_element(By.CSS_SELECTOR("a-icon a-icon-logo"))
# 'Create Account' Logo:
driver.find_element(By.CSS_SELECTOR("Create account"))
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