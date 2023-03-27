# Automated script for the Search functionality (positive)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

searchTerm = "Ring"

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
# Looking for the 'Search icon' web element:
searchIcon = driver.find_element(By.CSS_SELECTOR, "summary[aria-label='Search']")
# Clicking on the 'Search icon':
searchIcon.click()

time.sleep(3)
# Looking for the search box:
searchBox = driver.find_element(By.ID, "Search-In-Modal")
# Entering something into the search box:
searchBox.send_keys(searchTerm)

time.sleep(3)
# Looking for the search button:
searchButton = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Search']")
# Clicking on the search button:
searchButton.click()

time.sleep(5)
# Closing the window:
driver.close()