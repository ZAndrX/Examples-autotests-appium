from page.device_page import DevicePage


def test_connect(driver):
    device = DevicePage(driver)
    device.click_on_home()

    device.swipe_desktop(direction=1)
    device.swipe_desktop(direction=-1)
