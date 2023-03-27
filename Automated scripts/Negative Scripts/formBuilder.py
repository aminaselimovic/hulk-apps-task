# Automated script for the Form builder (negative)
import time
from datePickerFunction import datePicker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

firstName = "@mina"
lastName = "Sel1movic"
email = "aminasel@example"
date = "04/05/2025"
# Copy and paste your file path here (textfile.txt):
filePath = "C:\\Users\\amina\\OneDrive\\Desktop\\QA Practical Test\\textfile.txt"
website = "invalid url"
rating = "-5"

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
# Redirecting to the Form builder page:
driver.get("https://qa-practical-test.myshopify.com/pages/form-builder")
# Switching to the Form frame:
driver.switch_to.frame("frame_8Q1zrNOWpYyVd3BKCe2hAA")

time.sleep(3)
# Searching for the First Name, Last Name and Email fields and entering data:
firstNameInput = driver.find_element(By.ID, "form_input_0").send_keys(firstName)
lastNameInput = driver.find_element(By.ID, "form_input_1").send_keys(lastName)
emailInput = driver.find_element(By.ID, "form_input_2").send_keys(email)
# Calling the datePicker function from datePickerFunction.py file:
datePicker(date, driver)
# Searching for the 'Upload file' button:
uploadFile = driver.find_element(By.CSS_SELECTOR, "input[type='file']")

# Exiting the Form frame to scroll down the page:
driver.switch_to.default_content()
driver.execute_script("window.scrollTo(0,500)")
# Switching to the Form frame once again:
driver.switch_to.frame("frame_8Q1zrNOWpYyVd3BKCe2hAA")

# Uploading the file by entering the file path:
uploadFile.send_keys(filePath)
time.sleep(5)

# Searching for the Website and Give ratings fields and entering data:
websiteInput = driver.find_element(By.ID, "form_input_5").send_keys(website)
ratingInput = driver.find_element(By.ID, "form_input_6").send_keys(rating)

# Searching for the 'Submit' button:
submitButton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
# Clicking on the 'Submit' button:
submitButton.click()

time.sleep(5)
# Closing the driver:
driver.close()