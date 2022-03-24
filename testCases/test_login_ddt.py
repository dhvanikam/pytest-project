from pageObjects.login import Login
from pageObjects.home import Home
from utilities.customLogger import LogGen
from utilities.XLUtils import XLUtils
import warnings
import time

class Test_001_DDT_Login:
    logger = LogGen.loggen()
    path='.//Testdata/Logindata.xlsx'

    def test_01_login_ddt_valid(self,setup):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.driver = setup
        self.baseURL = XLUtils.readData(self.path,'URLs',1,2)
        self.driver.get(self.baseURL)
        self.logger.info("****test_01_login_valid*****")
        self.logger.info("*****Loading URL******")

        #Load Login URL
        self.driver = setup
        self.loginURL = XLUtils.readData(self.path,'URLs',2,2)
        self.driver.get(self.loginURL)
        
        #Enter valid Username and Password
        loginpage = Login(self.driver)
        self.username=XLUtils.readData(self.path,'LoginPage',2,1)
        self.password=XLUtils.readData(self.path,'LoginPage',2,2)
        self.logger.info("*****username******")
        print("username",self.username)
        self.logger.info("*****password******")
        print("password",self.password)
        loginpage.enter_username(self.username)
        loginpage.enter_password(self.password)
        self.logger.info("*****Try login with given username and password******")

        #Try login with given password
        loginpage.click_login()

        #Check successful login message
        time.sleep(2)
        message = loginpage.check_message()
        print(message)
        if "You logged into a secure area!" in message:
            assert True
        else:
            self.logger.error("*****Message not match******")
            self.driver.save_screenshot(".//Screenshots//"+"test_01_login_ddt_valid_test.png")
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
    
    def test_02_login_ddt_invalid_password(self,setup):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.driver = setup
        self.baseURL = XLUtils.readData(self.path,'URLs',1,2)
        self.driver.get(self.baseURL)
        self.logger.info("****test_02_invalid_password*****")
        self.logger.info("*****Loading URL******")

        #Load URL
        self.driver = setup
        loginURL = XLUtils.readData(self.path,'URLs',2,2)
        self.driver.get(loginURL)
        
        #Enter valid Username and invalid Password
        loginpage = Login(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'LoginPage')
        print("Total rows",self.rows)
        self.username=XLUtils.readData(self.path,'LoginPage',3,1)
        self.password=XLUtils.readData(self.path,'LoginPage',3,2)
        self.logger.info("*****username******")
        print("username",self.username)
        self.logger.info("*****password******")
        print("password",self.password)
        loginpage.enter_username(self.username)
        loginpage.enter_password(self.password)
        self.logger.info("*****Try login with given password******")

        #Try login with given password
        loginpage.click_login()

        #Check error message
        time.sleep(2)
        message = loginpage.check_message()
        print(message)
        if "Your password is invalid!" in message:
            assert True
        else:
            self.logger.error("*****Message not match******")
            self.driver.save_screenshot(".//Screenshots//"+"test_02_login_ddt_invalid_password_test.png")
            self.driver.close()
            assert False
    
        self.driver.close()

    def test_03_login_ddt_invalid_username(self,setup):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.driver = setup
        self.baseURL = XLUtils.readData(self.path,'URLs',1,2)
        self.driver.get(self.baseURL)
        self.logger.info("****test_03_invalid_username*****")
        self.logger.info("*****Loading URL******")
        #Load URL
        self.driver = setup
        self.loginURL = XLUtils.readData(self.path,'URLs',2,2)
        self.driver.get(self.loginURL)
        
        #Enter valid Username and Password
        loginpage = Login(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'LoginPage')
        print("Total rows",self.rows)
        self.username=XLUtils.readData(self.path,'LoginPage',4,1)
        self.password=XLUtils.readData(self.path,'LoginPage',4,2)
        self.logger.info("*****username******")
        print("username",self.username)
        self.logger.info("*****password******")
        print("password",self.password)
        loginpage.enter_username(self.username)
        loginpage.enter_password(self.password)
        self.logger.info("*****Try login with given password******")

        #Try login with given password
        loginpage.click_login()

        #Check error message
        time.sleep(2)
        message = loginpage.check_message()
        print(message)
        if "Your username is invalid!" in message:
            assert True
        else:
            self.logger.error("*****Message not match******")
            self.driver.save_screenshot(".//Screenshots//"+"test_03_login_ddt_invalid_username_test.png")
            self.driver.close()
            assert False
    
        self.driver.close()

    def test_04_login_ddt_no_username_password(self,setup):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.driver = setup
        self.baseURL = XLUtils.readData(self.path,'URLs',1,2)
        self.driver.get(self.baseURL)
        self.logger.info("****test_04_no_username_password*****")
        self.logger.info("*****Loading URL******")

        #Load URL
        self.driver = setup
        self.loginURL = XLUtils.readData(self.path,'URLs',2,2)
        self.driver.get(self.loginURL)
        
        #Enter valid Username and Password
        loginpage = Login(self.driver)
        loginpage.enter_username('')
        loginpage.enter_password('')
        self.logger.info("*****Try login******")

        #Try login with given password
        loginpage.click_login()

        #Check error message
        time.sleep(2)
        message = loginpage.check_message()
        print(message)
        if "Your username is invalid!" in message:
            assert True
        else:
            self.logger.error("*****Message not match******")
            self.driver.save_screenshot(".//Screenshots//"+"test_04_login_ddt_no_username_password_test.png")
            self.driver.close()
            assert False
    
        self.driver.close()