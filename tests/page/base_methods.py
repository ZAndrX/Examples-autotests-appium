from appium import webdriver
import allure
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions


class BaseMethods:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    @allure.step('Ожидание кликабельности элемента')
    def wait_clickable_element(self, locator: tuple[str, str], timeout: int = 5) -> webdriver.WebElement:
        """
        Ожидание кликабельности элемента на странице по локатору
        :param locator: Локатор элемента
        :param timeout: Максимальное время ожидания кликабельности элемента
        :return: Кликабельный элемент найденный по локатору на странице
        """
        return Wait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step('Ожидание появления элемента')
    def wait_element_present(self, locator: tuple[str, str], timeout: int = 5) -> webdriver.WebElement:
        """
        Ожидание элемента на странице по локатору
        :param locator: Локатор элемента
        :param timeout: Максимальное время ожидания появления элемента
        :return: Элемент найденный по локатору на странице
        """
        return Wait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Нажатие на кнопку по коду кнопки')
    def click_on_button_as_keycode(self, keycode: int) -> None:
        """
        Нажатие на кнопку по коду кнопки
        :param keycode: Код кнопки из appium.webdriver.extensions.android.nativekey.AndroidKey
        :return: None
        """
        self.driver.press_keycode(keycode)

    @allure.step('Свайп по коодинатам')
    def swipe_by_coordinates(self, x1: int, y1: int, x2: int, y2: int, duration: int = 0) -> None:
        """
        Свайп по коодинатам
        :param x1: Начальная координата x
        :param y1: Начальная координата y
        :param x2: Конечная координата x
        :param y2: Конечная координата y
        :param duration: длительность свайпа
        :return: None
        """
        self.driver.swipe(x1, y1, x2, y2, duration)

    @allure.step('Свайп по коодинатам элемента')
    def swipe_by_element(self, locator: tuple[str, str], direction: int = 1, deviation_y: int = 0) -> None:
        """
        Свайп по коодинатам элемента
        :param locator: Локатор элемента
        :param direction: Направление свайпа по оси x, где 1 - вправо, а -1 - влево
        :param deviation_y: Отклонение от середины элемента по оси y
        :return: None
        """
        bounds: str = self.wait_element_present(locator).get_attribute("bounds")[1:-1]
        start, end = list([coord.split(',') for coord in bounds.split("][")])
        y = int((int(end[1]) - int(start[1])) / 2) + deviation_y
        end_x, start_x = None, None
        if direction == 1:
            end_x = int(start[0]) + 10
            start_x = int(end[0]) - 10
        elif direction == -1:
            start_x = int(start[0]) + 10
            end_x = int(end[0]) - 10
        self.swipe_by_coordinates(x1=start_x, x2=end_x, y1=y, y2=y)
