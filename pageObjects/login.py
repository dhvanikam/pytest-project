from Locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException

class Login():

    def __init__(self, driver):
      self.driver = driver     
      self.username_textbox_id = Locators.username_textbox_id
      self.password_textbox_id = Locators.password_textbox_id
      self.login_button_xpath = Locators.login_button_xpath
      self.message_xpath = Locators.message

    def check_loginbutton_present(self):
        try:
          if(self.driver.find_element_by_xpath(self.login_button_xpath).is_displayed):
              print("Login button present")
              return True
        except NoSuchElementException: print("Login button not present")

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def check_message(self):
        msg = self.driver.find_element_by_xpath(self.message_xpath).text
        return msg