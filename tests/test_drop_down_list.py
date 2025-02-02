import allure
import pytest
from pages.main_page import MainPage
from locators.locators_main_page import LocatorsMainPage
from data import TestData

class TestDropDownList:
    @allure.title("Проверка соответствия выпадающего списка ожидаемому ответу (параметру TestData.text_[i])")
    @allure.description("На странице ищем элемент выпадающего списка, открываем его кликом, проверяем, что текст ответа (answer)"
                        "равен ожидаемому (answer_exc)")
    @pytest.mark.parametrize(
        'locator, answer_cur, answer_exc',
        [
            (LocatorsMainPage.list_question_1, LocatorsMainPage.text_answer_1, TestData.text_1),
            (LocatorsMainPage.list_question_2, LocatorsMainPage.text_answer_2, TestData.text_2),
            (LocatorsMainPage.list_question_3, LocatorsMainPage.text_answer_3, TestData.text_3),
            (LocatorsMainPage.list_question_4, LocatorsMainPage.text_answer_4, TestData.text_4),
            (LocatorsMainPage.list_question_5, LocatorsMainPage.text_answer_5, TestData.text_5),
            (LocatorsMainPage.list_question_6, LocatorsMainPage.text_answer_6, TestData.text_6),
            (LocatorsMainPage.list_question_7, LocatorsMainPage.text_answer_7, TestData.text_7),
        ]
    )
    def test_drop_down_list(self, driver, open_browser, locator, answer_cur, answer_exc):
        main_page = MainPage(driver)
        main_page.wait_load_main_page()
        answer = main_page.check_text_drop_down_list(locator, answer_cur)
        assert answer == answer_exc
