from ast import Assert
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.login import Login
from pageObjects.home import Home
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import warnings
import time

class Test_001_Login:
    logger = LogGen.loggen()
    def test_01_login_valid(self,setup):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.driver = setup
        baseURL = ReadConfig.getBaseUrl()
        print(baseURL)
        username = ReadConfig.getusername()
        print(username)
        password = ReadConfig.getpassword()
        print(password)

        self.driver.get(baseURL)
        self.logger.info("****test_01_login_valid*****")
        self.logger.info("*****Loading URL******")
        #Load URL
        self.driver = setup
        loginURL = ReadConfig.getLoginUrl()
        self.driver.get(loginURL)
        
        #Enter valid Username and Password
        loginpage = Login(self.driver)
        loginpage.enter_username(username)
        loginpage.enter_password(password)
        self.logger.info("*****Try login with given password******")

        #Try login with given password
        loginpage.click_login()

        #Check successful login message
        time.sleep(2)
        message = loginpage.check_message()
        print(message)
        if "You logged into a secure area!" in message:
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test.png")
            self.driver.close()
            assert False
            

        # self.assertIn("You logged into a secure area!", message)
        self.logger.info("*****Login successful******")
        #Check logout button present on home page
        homepage = Home(self.driver)
        homepage.check_logoutbutton_present()

        #Click on logout button
        homepage.click_logout()

        #Check successful logout message
        message = loginpage.check_message()
        print(message)
        # self.assertIn("You logged out of the secure area!", message)
        self.logger.info("*****Logout successful******")
        self.driver.close()

    def test_02_login_valid(self,setup):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.driver = setup
        baseURL = ReadConfig.getBaseUrl()
        print(baseURL)
        username = ReadConfig.getusername()
        print(username)
        password = ReadConfig.getpassword()
        print(password)

        self.driver.get(baseURL)
        self.logger.info("****test_02_login_valid*****")
        self.logger.info("*****Loading URL******")
        #Load URL
        self.driver = setup
        loginURL = ReadConfig.getLoginUrl()
        self.driver.get(loginURL)
        
        #Enter valid Username and Password
        loginpage = Login(self.driver)
        loginpage.enter_username(username)
        loginpage.enter_password(password)
        self.logger.info("*****Try login with given password******")

        #Try login with given password
        loginpage.click_login()

        #Check successful login message
        time.sleep(2)
        message = loginpage.check_message()
        print(message)
        if "You logged into a secure area!" in message:
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test.png")
            self.driver.close()
            assert False
            

        # self.assertIn("You logged into a secure area!", message)
        self.logger.info("*****Login successful******")
        #Check logout button present on home page
        homepage = Home(self.driver)
        homepage.check_logoutbutton_present()

        #Click on logout button
        homepage.click_logout()

        #Check successful logout message
        message = loginpage.check_message()
        print(message)
        # self.assertIn("You logged out of the secure area!", message)
        self.logger.info("*****Logout successful******")
        self.driver.close()
    # def test_02_login_invalid_password(self, setup):
    #     #Load URL
    #     self.driver = setup
    #     self.driver.get(ReadConfig.getLoginUrl())

    #     #Enter valid Username and invalid Password
    #     loginpage = Login(self.driver)
    #     loginpage.enter_username('tomsmith')
    #     loginpage.enter_password('SuperSecretPassword!1')

    #     #Try login with given password
    #     loginpage.click_login()

    #     #Check error message
    #     message = loginpage.check_message()
    #     print(message)
    #     self.assertIn("Your password is invalid!", message)
    #     #self.assertAlmostEqual(message, "Your username is invalid!")

    # def test_03_login_invalid_username(self, setup):
    #     #Load URL
    #     self.driver = setup
    #     self.driver.get(ReadConfig.getBaseUrl())

    #     #Enter invalid Username and valid Password
    #     loginpage = Login(self.driver)
    #     loginpage.enter_username('tomsmith1')
    #     loginpage.enter_password('SuperSecretPassword!')

    #     #Try login with given password
    #     loginpage.click_login()

    #     #Check error message
    #     message = loginpage.check_message()
    #     self.assertIn("Your username is invalid!", message)

    
    # def test_04_login_no_username_password(self, setup):
    #  #Load URL
    #     driver = setup
    #     driver.get(ReadConfig.getLoginUrl())

    #     #Enter invalid Username and valid Password
    #     loginpage = Login(driver)
    #     loginpage.enter_username('')
    #     loginpage.enter_password('')

    #     #Try login with given password
    #     loginpage.click_login()

    #     #Check error message
    #     message = loginpage.check_message()
    #     self.assertIn("Your username is invalid!", message)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()
    #     print("Test Complete")

# if __name__ == '__main__' :
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dhvani/Workspace/python-selenium/Reports'))