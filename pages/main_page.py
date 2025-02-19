import allure
from locators.locators_main_page import LocatorsMainPage
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LocatorsMainPage()

    @allure.step('Ожидаем открытие главной страницы')
    def wait_load_main_page(self):
        self.wait_visibility_of_element(LocatorsMainPage.header_scooter)

    @allure.step('Нажимаем кнопку "{locator}"')
    def click_button_order(self, locator):
        self.click_on_element(locator)

    # шаг для проверки работы выпадающего списка
    @allure.step('Ищем и сравниваем с ожидаемым текстом {text_locator} выпадающий список в разделе "Вопросы о важном"')
    def check_text_drop_down_list(self, locator, text_locator):
        self.scrolling_to_element(locator)
        self.wait_visibility_of_element(locator)
        self.click_on_element(locator)
        self.wait_visibility_of_element(text_locator)
        answer = self.get_text(text_locator)
        return answer

