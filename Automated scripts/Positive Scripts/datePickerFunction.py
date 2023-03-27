import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# A function that accepts two variables: myDate as a string in the correct format (MM/DD/YYYY) and the web driver.
def datePicker(myDate, driver):
    # Searching for the 'Date Of Birth' field:
    datePickerDropdown = driver.find_element(By.ID, "form_input_3")
    # Clicking on the 'Date Of Birth' field:
    datePickerDropdown.click()

    time.sleep(5)
    # After clicking on the field, the current date will be entered into the input box.
    # Getting the value from the input box:
    currentDate = datePickerDropdown.get_attribute('value')
    # Splitting the current date every time a '/' shows up and storing the month and year values into variables:
    # ["MM", "DD", "YYYY"]
    currentMonth = currentDate.split("/")[0]
    currentYear = currentDate.split("/")[2]
    # Splitting the desired date every time a '/' shows up and storing the month and year values into variables:
    # ["MM", "DD", "YYYY"]
    myMonth = myDate.split("/")[0]
    myYear = myDate.split("/")[2]

    # Searching for the web element to be able to search through the days of the month:
    divElement = driver.find_element(By.CSS_SELECTOR, "div[class='datepicker-days']")

    # If the desired year is higher than the current year or
    # if the years are the same value and the desired month comes after the current month, do this:
    if int(myYear) > int(currentYear) or (int(myMonth) > int(currentMonth) and int(myYear) == int(currentYear)):
        flag = True
        # A loop for clicking the 'next' button until we find the desired date:
        while flag == True:
            # Searching for the 'next' button/arrow and clicking on it:
            next = divElement.find_element(By.CSS_SELECTOR, "th[class='next']").click()
            # Searching for the table body:
            tableBody = divElement.find_element(By.TAG_NAME, "tbody")
            allDates = tableBody.find_elements(By.TAG_NAME, "td")
            # Going through all the dates inside the table body:
            for date in allDates:
                # Getting the value of the date element:
                dayData = date.get_attribute("data-day")
                # After finding the desired date that is equal to the value we got previously, break the for loops: 
                if dayData == myDate:
                    date.click()  
                    flag = False
                    break

    # If the desired year is lower than the current year or
    # if the years are the same value and the desired month comes before the current month, do this:
    elif int(myYear) < int(currentYear) or (int(myMonth) < int(currentMonth) and int(myYear) == int(currentYear)):
        flag = True
        # A loop for clicking the 'previous' button until we find the desired date:
        while flag == True:
            # Searching for the 'previous' button/arrow and clicking on it:
            previous = divElement.find_element(By.CSS_SELECTOR, "th[class='prev']").click()
            # Searching for the table body:
            tableBody = divElement.find_element(By.TAG_NAME, "tbody")
            allDates = tableBody.find_elements(By.TAG_NAME, "td")
            # Going through all the dates inside the table body:
            for date in allDates:
                # Getting the value of the date element:
                dayData = date.get_attribute("data-day") 
                # After finding the desired date that is equal to the value we got previously, break the for loops: 
                if dayData == myDate:
                    date.click()  
                    flag = False
                    break
    else:
        print("Invalid date format.")

