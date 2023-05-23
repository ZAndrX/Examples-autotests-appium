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

