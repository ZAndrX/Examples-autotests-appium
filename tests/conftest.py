import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


def pytest_addoption(parser):
    parser.addoption('--udid', action='store',
                     help="Choose udid device")
    parser.addoption('--url', action='store', default='http://127.0.0.1:4723',
                     help="Choose url appium")


@pytest.fixture(scope="function")
def driver(request):
    udid = request.config.getoption("udid")
    url = request.config.getoption("url")
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.udid = udid
    options.newCommandTimeout = 3600
    driver = webdriver.Remote(url, options=options)
    driver.unlock()

    yield driver
    driver.quit()
