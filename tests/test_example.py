import allure
import pytest
from page.device_page import DevicePage


@allure.title('Проверка смены рабочего стола')
@pytest.mark.parametrize('repetition', [5, 2])
def test_change_desktop(driver, repetition):
    """
        Нажать кнопку home;
        Свайпнуть экран влево-вправо;
        Параметризовать так, чтобы можно было задавать количество повторений свайпа влево-вправо.
    """
    device = DevicePage(driver)
    device.click_on_home()

    device.cycle_swipe_desktop(repetition=repetition)
