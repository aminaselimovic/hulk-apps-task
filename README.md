# Testing Overview - QA Practical Test


This overview describes the testing process that was conducted on the following website: https://qa-practical-test.myshopify.com. The type of testing used for this process was exploratory testing since there were no requirement documents available. Testing was conducted subjectively, since the task did not include Acceptance Criteria for any functionality.

The testing was conducted both manually and by using tools for automated testing. The tools in question are:

* *Visual Studio Code* as a coding editor, 
* *Python* as the preferred programming language used to create automation scripts,
* *Selenium Webdriver* as a tool for automating across the Chrome browser, 
* *Bandicam Screen Recorder* as a tool for recording bug reports,
* *Ufile.io*  for storing the bug reports.

The process of testing includes the testing of following functionalities:

* **Login & Signup:** website functionalities that allow the user to create a new account as well as log in with an already created account.
* **Form builder:** a functionality that allows the user to submit a form by entering the necessary information.
* **Add to cart/Buy now:** allows the user to choose a product, increase/decrease the quantity according to the desired discount, add the product to the cart and proceed to the checkout page.

Automated test scripts (both positive and negative) were created for all mentioned functionalities as well as for the search functionality. Automated test scripts can be found inside the folder ‘Automated scripts’. 

Bug reports can be found inside the folder ‘Bug reports’.

Manual test cases with expected and actual results, as well as steps on how to reproduce the testing, can be found inside the .xlsx file under the name ‘Test cases’.
