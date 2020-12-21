# TruVisibility_AutoTests
Autotests for TruCHAT

#Autotests are designed to test the main functionality of the TruCHAT project https://chat.truvisibility.net/
The chatbot widget for testing is located on the test page at https://trutest.truvisibility.net/

#Python is used as a programming language for writing automated tests. To work with it, you need to install a working environment https://www.python.org/downloads/
During the installation process, you need to specify the option " add Python 3.8 to Path”

#To work with autotests, you need to install the PyCharm application, which is an integrated development environment for the Python programming language (you can download the app by following the link https://www.jetbrains.com/pycharm/download/#section=windows)

#Selenium WebDriver is used as a tool for automating web browser actions. To work with the Chrome browser, use the ChromeDriver. Download it from the link https://chromedriver.chromium.org/downloads. The driver version must match the browser version!!!

#Open the project in Paycharm and open the terminal (alt + F12 key combination)
Run the command: pip install selenium

#The structure of the project:
*config / config.json - A configuration file that contains information about the application, test user data and information about the path to the Chrome driver. Be sure to specify your driver path, depending on where it is located on your computer!!!
*pages / ChatbotPage - Page Object (a design pattern that allows you to separate the logic of running tests from their implementation)
*Config.py - Contains the Config class to which configuration parameters are read
*ConfigManager.py - Contains the ConfigManager class that reads the configuration
*test_FileName.py - Files of tests

#How to run tests
*Open one of the files of type test_FileName.py
*Perform the prerequisites that are specified in the test
*Run the entire test suite or each test individually by clicking on the corresponding green triangle on the Line Numbers
*Wait until the tests are finished and the results are displayed in the console
Note: To follow the actions performed comment out the line "options.add_argument('headless')" (ctrl + / key combination)


