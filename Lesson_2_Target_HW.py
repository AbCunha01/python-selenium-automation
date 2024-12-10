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
driver.implicitly_wait(6)

driver.get("https://www.target.com/")


driver.find_element((By.XPATH, '//*[@data-test="@web/AccountLink"]')).click()
driver.find_element(By.XPATH, '//*[@data-test="accountNav-signIn"]').click()


expected = "Sign into your Target account"
actual = driver.find_element(By.ID,"Sign into your Target account")
assert expected == actual, f'Expected {expected} did not match actual {actual}'


driver.find_element(By.ID, 'login')
