from Locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException

class Home():
  
  def __init__(self, driver):
      self.driver = driver
      
      self.logout_link_xpath = Locators.logout_link_xpath

  def check_logoutbutton_present(self):
    try:
      if(self.driver.find_element_by_xpath(self.logout_link_xpath).is_displayed):
        print("Logout button present")
        return True
    except NoSuchElementException: print('Logout button not present')

  def click_logout(self):
       self.driver.find_element_by_xpath(self.logout_link_xpath).click()
