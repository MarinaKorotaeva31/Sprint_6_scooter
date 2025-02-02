import allure
import pytest
from pages.order_page import OrderPage
from urls import Urls
from locators.locators_base_page import LocatorsBasePage

class TestDropDownList:
    @allure.title('Проверяем переход со страницы заказа на главную страницу Самоката и Дзена')
    @allure.description('Переходим на страницу создания заказа; кликаем на лого Самоката и Дзена; проверяем,'
                        'что текущий url == ожидаемому')
    @pytest.mark.parametrize(
        'logo, current_url_exc',
        [
            (LocatorsBasePage.logo_scooter, Urls.main_page),
            (LocatorsBasePage.logo_yandex, Urls.dzen_page)
        ]
    )
    def test_switch_on_page(self, driver, open_order_page, logo, current_url_exc):
        order_page = OrderPage(driver)
        order_page.click_on_element(logo)
        if current_url_exc == Urls.dzen_page:
            order_page.check_switch_to_dzen()
        received_url = order_page.get_current_url()
        assert received_url == current_url_exc
