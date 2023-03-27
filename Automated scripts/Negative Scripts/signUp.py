# Automated script for the Signup functionality (negative)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

firstName = "Am1na"
lastName = "$elimovic"
email = "test@example"
password = "pass"

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
# Searching for all web elements that have the tag name "a":
aElements = driver.find_elements(By.TAG_NAME, "a")
for element in aElements:
    # All the letters in 'element.text' are lowercase and all the spaces are replaced with an empty string.
    # Searching for the specific element that contains the following text:
    if element.text.lower().replace(" ", "") == "createaccount": 
        # Clicking on the 'Create account' button:
        element.click()
        break

time.sleep(3)
# Entering data into all the fields:
firstNameInput = driver.find_element(By.NAME, "customer[first_name]").send_keys(firstName)
lastNameInput = driver.find_element(By.NAME, "customer[last_name]").send_keys(lastName)
emailInput = driver.find_element(By.NAME, "customer[email]").send_keys(email)
passwordInput = driver.find_element(By.NAME, "customer[password]").send_keys(password)
# Searching for all web elements that have the tag name "button":
buttons = driver.find_elements(By.TAG_NAME, "button")
for button in buttons:
    # All the letters in 'button.text' are lowercase and all the spaces are replaced with an empty string.
    # Searching for the specific element that contains the following text:
    if button.text.lower().replace(" ", "") == "create":
        # Clicking on the 'Create' button:
        button.click()
        break

time.sleep(5)
# Closing the window:
driver.close()