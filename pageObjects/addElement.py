from Locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException

class AddElement():
  
  def __init__(self, driver):
      self.driver = driver
      
      self.addElement_link_xpath = Locators.addElement_link_xpath
      self.deleteElement_link_xpath = Locators.deleteElement_link_xpath

  def addbutton_text(self):
       button_text = self.driver.find_element_by_xpath(self.addElement_link_xpath).text
       return button_text

  def deletebutton_text(self):
       button_text = self.driver.find_element_by_xpath(self.deleteElement_link_xpath).text
       return button_text

  def click_AddElement(self):
       self.driver.find_element_by_xpath(self.addElement_link_xpath).click()
       
  def click_DeleteElement(self):
       self.driver.find_element_by_xpath(self.deleteElement_link_xpath).click()

  def check_ElementPresent(self):
      if(self.driver.find_element_by_xpath(self.addElement_link_xpath).is_displayed):
          return True

  def check_deleteElementPresent(self):
      try:
          if(self.driver.find_element_by_xpath(self.deleteElement_link_xpath).is_displayed):
              print("Element exist")
              return True
      except NoSuchElementException: print('Element does not exist')