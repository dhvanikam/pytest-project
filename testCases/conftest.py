from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("*******Launching in Chrome******")   
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("*******Launching in firefox******")
    elif browser=='safari':
        driver = webdriver.Safari()
        print("*******Launching in Safari******")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

####### Pytest HTML Reports#####

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'PytestProject'
#     config._metadata['Module Name'] = 'Login'
#     config._metadata['Tester'] = 'Dhvanika'

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)