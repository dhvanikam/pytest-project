from urllib import response
from h11 import Response
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/checkboxes")
checkbox1 = driver.find_element_by_xpath("//*[@id='checkboxes']/input[1]")

time.sleep(2)
checkbox1.click()
time.sleep(2)
if checkbox1.is_selected():
    print("Checkbox is selected")
else:
    print("Checkbox is not selected")

driver.close()