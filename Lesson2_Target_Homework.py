from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep  # Optional, use WebDriverWait instead for a cleaner approach

driver_path = ChromeDriverManager().install()

# Create Chrome browser instance (service object recommended)
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver.get("https://www.target.com/")

try:

  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//use[@href="/icons/Account.svg#Account"]')))
  driver.find_element(By.XPATH,'//a[@data-test="accountNav-signIn"]').click()
except:
  pass

if "Account" in driver.title:
  print("Successfully navigated to Sign In page")
else:
  print("Verification failed: Sign In page title not found")

driver.quit()
