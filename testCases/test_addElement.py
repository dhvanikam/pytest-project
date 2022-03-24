from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
import unittest
from pages.addElement import AddElement
import HtmlTestRunner

class AddElementTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://the-internet.herokuapp.com/")
        cls.driver.maximize_window()
    
    def test_01_add_element(self):
        #Load the URL
        driver = self.driver
        driver.get()

        #Check AddElement button present
        addElementpage = AddElement(driver)
        addElementpage.check_ElementPresent()

        #Check button text match
        text = addElementpage.addbutton_text()
        print(text)
        self.assertEqual("Add Element", text, "Element Text mismatch")

        #Add Element by clicking button
        addElementpage.click_AddElement()

        #Check Element Added
        addElementpage.check_deleteElementPresent()

        #Check element text match
        text = addElementpage.deletebutton_text()
        print(text)
        self.assertEqual("Delete", text, "Element Text mismatch")    
        

    def test_02_delete_element(self):
        #Load the URL
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

        #Check AddElement button present
        addElementpage = AddElement(driver)
        addElementpage.check_ElementPresent()

        #Check button text match
        addElementpage = AddElement(driver)
        text = addElementpage.addbutton_text()
        print(text)

        #Add Element by clicking button
        addElementpage.click_AddElement()

        #Check element added
        addElementpage.check_deleteElementPresent()

        #Check element text match
        text = addElementpage.deletebutton_text()
        print(text)
        self.assertEqual("Delete", text, "Element Text mismatch")    
        
        #Delete element by clicking on delete buttton
        addElementpage.click_DeleteElement()

        #Check element deleted
        addElementpage.check_deleteElementPresent()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")

if __name__ == '__main__' :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dhvani/Workspace/python-selenium/Reports'))