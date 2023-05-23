from appium.webdriver.common.appiumby import By
from appium.webdriver.extensions.android.nativekey import AndroidKey


class CommonButtons:
    button_home = AndroidKey.HOME


class Desktop:
    content = (By.ID, 'android:id/content')
