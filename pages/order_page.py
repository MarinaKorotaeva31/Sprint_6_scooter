import allure
from locators.locators_order_page import LocatorsOrderPage
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LocatorsOrderPage()

    @allure.step('Заполняем страницу "Для кого самокат"')
    def filling_data_on_page_for_whom(self, name, lastname, address, number, station):
        self.wait_visibility_of_element(self.locators.input_name)
        self.send_keys_to_input(self.locators.input_name, name)
        self.send_keys_to_input(self.locators.input_lastname, lastname)
        self.send_keys_to_input(self.locators.input_address, address)
        self.send_keys_to_input(self.locators.input_station, station)
        self.click_on_element(self.locators.button_station)
        self.send_keys_to_input(self.locators.input_number, number)

    @allure.step('Заполняем страницу "Про аренду"')
    def filling_data_on_page_about_rent(self, date, renta, color, comment: str):
        self.send_keys_to_input(self.locators.input_date, date)
        self.click_on_element(self.locators.emty_place)
        self.click_on_element(self.locators.renta)
        self.click_on_element(renta)
        self.click_on_element(color)
        self.send_keys_to_input(self.locators.input_comment, comment)

    @allure.step('Проверяем появление оповещения об успешном заказе')
    def order_success(self, name, lastname, address, number, station, data, renta, color, comment):
        self.filling_data_on_page_for_whom(name, lastname, address, number, station)
        self.click_on_element(self.locators.button_next)
        self.filling_data_on_page_about_rent(data, renta, color, comment)
        self.click_on_element(self.locators.button_order)
        self.wait_visibility_of_element(self.locators.button_yes)
        self.click_on_element(self.locators.button_yes)
        success_mes = self.get_text(self.locators.success_order)
        return success_mes

    @allure.step('Проверяем успешный переход на страницу Дзена')
    def check_switch_to_dzen(self):
        self.get_tab_and_switch()
        self.check_switch_dzen()

    @allure.step('Получаем текущий url')
    def get_current_url(self):
        return self.driver.current_url
