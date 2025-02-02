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
            (Main.button_order_1, Data.name_1, Data.lastname_1, Data.address_1, Data.number_1,
             Data.station_1, Data.date_1, Order.period_1, Order.chb_black, Data.comment_1),
            (Main.button_order_2, Data.name_2, Data.lastname_2, Data.address_2, Data.number_2,
             Data.station_2, Data.date_2, Order.period_2, Order.chb_grey, Data.comment_2)
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
