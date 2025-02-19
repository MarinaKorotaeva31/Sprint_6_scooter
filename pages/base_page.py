import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators_base_page import LocatorsBasePage

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент "{locator}" на странице')
    def find_of_element(self, locator):
        self.driver.find_element(*locator)

    @allure.step('Нажимаем на элемент "{locator}"')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Заполняем поле ввода "{locator}": {keys}')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Листаем до элемента "{locator}"')
    def scrolling_to_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем появления элемента "{locator}" на странице')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получаем текст элемента "{locator}"')
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Переходим в браузере на текущую страницу')
    def get_tab_and_switch(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        return tabs

    @allure.step('Проверям, что находимся на странице Дзена')
    def check_switch_dzen(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(LocatorsBasePage.yandex))
