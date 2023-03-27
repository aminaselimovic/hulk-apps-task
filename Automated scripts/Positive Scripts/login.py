# Automated script for the Login functionality (positive)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

correctEmail = "aminasel@example.com"
correctPassword = "Selimovic-23"

driver = webdriver.Chrome()
driver.implicitly_wait(60)
# Opening the website:
driver.get("https://qa-practical-test.myshopify.com")
# Maximizing the window:
driver.maximize_window()

time.sleep(3)
# Searching for the password field:
passwordInput = driver.find_element(By.ID, "password") 
# Entering the password:
passwordInput.send_keys("brauff") 

time.sleep(3)
# Searching for the 'Enter' button:
enterButton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
# Clicking on the 'Enter' button:
enterButton.click()

time.sleep(5)
# Searching for all web elements that have the tag name "a":
aElements = driver.find_elements(By.TAG_NAME, "a")
for element in aElements:
    # Searching for the specific element that contains "Log in" text:
    if element.text == "Log in":
        # Clicking on the Login/Signup icon:
        element.click()
        break

time.sleep(3)
# Searching for the email and password fields:
emailInput = driver.find_element(By.ID, "CustomerEmail")
passwordInput = driver.find_element(By.ID, "CustomerPassword")
# Entering email and password:
emailInput.send_keys(correctEmail)
passwordInput.send_keys(correctPassword)
# Searching for the Login form web element:
loginForm = driver.find_element(By.ID, "customer_login")
# Searching for the 'Sign in' button inside the login form:
signInButton = loginForm.find_element(By.TAG_NAME, "button")
# Clicking on the 'Sign in' button:
signInButton.click()

time.sleep(3)
# Closing the window:
driver.close()