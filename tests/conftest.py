import pytest
import allure
from selenium import webdriver
from urls import Urls

@pytest.fixture()
def driver():   # фикстура создания драйвера
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@allure.step('Открываем браузер')
@pytest.fixture
def open_browser(driver):  # фикстура открытия главной страницы
    driver.get(Urls.main_page)
    driver.maximize_window()

@pytest.fixture
def open_order_page(driver):  # фикстура открытия главной страницы
    driver.get(Urls.order_page)
