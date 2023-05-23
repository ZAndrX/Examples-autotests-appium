import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.udid = '192.168.1.1:5555'
    options.newCommandTimeout = 3600
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.unlock()

    yield driver
    driver.quit()
