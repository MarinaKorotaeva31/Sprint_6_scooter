import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.locators_main_page import LocatorsMainPage as Main
from locators.locators_order_page import LocatorsOrderPage as Order
from data import TestData as Data

class TestOrderPage:
    @allure.title('Проверка прохождения позитивного сценария создания заказа')
    @allure.description('Проверяем переход на страницу создания заказа посредством двух кнопок "Заказать"'
                        'на главной странице; заполняем поля для заказа; проверям, что появляется '
                        'уведомление об успешном заказе')
    @pytest.mark.parametrize(
        'button_order, name, lastname, address, number, station, date, period, color, comment',
        [
            (Main.button_order_1, Data.NAME_1, Data.LASTNAME_1, Data.ADDRESS_1, Data.NUMBER_1,
             Data.STATION_1, Data.DATE_1, Order.period_1, Order.chb_black, Data.COMMENT_1),
            (Main.button_order_2, Data.NAME_2, Data.LASTNAME_2, Data.ADDRESS_2, Data.NUMBER_2,
             Data.STATION_2, Data.DATE_2, Order.period_2, Order.chb_black, Data.COMMENT_2)
        ]
    )
    def test_order_is_success(self, driver, open_browser, button_order, name, lastname, address, number, station, date, period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_load_main_page()
        main_page.scrolling_to_element(button_order)
        main_page.wait_visibility_of_element(button_order)
        main_page.click_button_order(button_order)
        message = order_page.order_success(name, lastname, address, number, station, date, period, color, comment)
        assert message == 'Посмотреть статус'
