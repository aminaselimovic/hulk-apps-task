# Automated script for the Checkout process (negative)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

quantity = -5

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
# Searching for the 'Catalog' button:
catalogButton = driver.find_element(By.LINK_TEXT, "Catalog")
# Clicking on the 'Catalog' button:
catalogButton.click()

time.sleep(3)
# Searching for all products:
productGrid = driver.find_element(By.ID, "product-grid")
products = productGrid.find_elements(By.TAG_NAME, "li")
# Clicking on the first product:
firstProduct = products[0]
firstProduct.click()

time.sleep(3)
# Searching for the quantity input field:
quantityInput = driver.find_element(By.NAME, "quantity")
# Clearing the input field:
quantityInput.clear()
# Entering the quantity:
quantityInput.send_keys(quantity)

time.sleep(3)
# Searching for the 'Add to cart' button:
addToCartButton = driver.find_element(By.NAME, "add")
# Clicking on the 'Add to cart' button:
addToCartButton.click()

time.sleep(3)
# Searching for the 'View my cart' button:
viewMyCart = driver.find_element(By.ID, "cart-notification-button")
# Clicking on the button and redirecting to Cart page:
viewMyCart.click()

time.sleep(5)
# Searching for the 'Checkout' button on the Cart page:
checkoutButton = driver.find_element(By.ID, "checkout")
# Clicking on the button:
checkoutButton.click()

time.sleep(10)
# Closing the window:
driver.close()