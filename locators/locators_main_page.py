from selenium.webdriver.common.by import By

class LocatorsMainPage:
    list_question_1 = [By.ID, 'accordion__heading-0']  # кнопка выпадающего списка 1
    text_answer_1 = [By.ID, 'accordion__panel-0']  # текст внутри выпадающего списка 1
    list_question_2 = [By.ID, 'accordion__heading-1']  # кнопка выпадающего списка 2
    text_answer_2 = [By.ID, 'accordion__panel-1']  # текст внутри выпадающего списка 2
    list_question_3 = [By.ID, 'accordion__heading-2']  # кнопка выпадающего списка 3
    text_answer_3 = [By.ID, 'accordion__panel-2']  # текст внутри выпадающего списка 3
    list_question_4 = [By.ID, 'accordion__heading-3']  # # кнопка выпадающего списка 4
    text_answer_4 = [By.ID, 'accordion__panel-3']  # текст внутри выпадающего списка 4
    list_question_5 = [By.ID, 'accordion__heading-4']  # кнопка выпадающего списка 5
    text_answer_5 = [By.ID, 'accordion__panel-4']  # текст внутри выпадающего списка 5
    list_question_6 = [By.ID, 'accordion__heading-5']  # кнопка выпадающего списка 6
    text_answer_6 = [By.ID, 'accordion__panel-5']  # текст внутри выпадающего списка 6
    list_question_7 = [By.ID, 'accordion__heading-6']  # кнопка выпадающего списка 7
    text_answer_7 = [By.ID, 'accordion__panel-6']  # текст внутри выпадающего списка 7
    list_question_8 = [By.ID, 'accordion__heading-7']  # кнопка выпадающего списка 8
    text_answer_8 = [By.ID, 'accordion__panel-7']  # текст внутри выпадающего списка 9

    header_scooter = [By.CLASS_NAME, 'Home_Header__iJKdX']  # заголовок на главной странице "Самокат на пару дней"

    button_order_1 = [By.CLASS_NAME, 'Button_Button__ra12g']  # кнопка "Заказать" вверху главной страницы
    button_order_2 = [By.XPATH, './/div[@class = "Home_RoadMap__2tal_"]//button[text() = "Заказать"]']  # кнопка "Заказать" посередине главной страницы
