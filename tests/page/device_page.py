import time
from .base_methods import BaseMethods
from .locators import CommonButtons, Desktop
import allure


class DevicePage(BaseMethods):
    @allure.step('Нажатие на кнопку домой')
    def click_on_home(self) -> None:
        self.click_on_button_as_keycode(CommonButtons.button_home)

    @allure.step('Переключение на другой рабочий стол')
    def swipe_desktop(self, direction: int = 1) -> None:
        """
        Переключение на другой рабочий стол
        :param direction:  Направление свайпа по оси x, где 1 - вправо, а -1 - влево
        :return: None
        """
        self.swipe_by_element(Desktop.content, direction)

    @allure.step('Цикличное переключение на другой экран и обратно')
    def cycle_swipe_desktop(self, repetition: int = 1, period: int = 0) -> None:
        """
        Цикличное переключение на другой экран и обратно
        :param repetition: Количество повторений
        :param period: Количество секунд между повторением
        """
        for i in range(repetition):
            self.swipe_desktop(direction=1)
            self.swipe_desktop(direction=-1)
            time.sleep(period)
