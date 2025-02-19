from selenium.webdriver.common.by import By

class LocatorsOrderPage:
    input_name = [By.XPATH, './/input[@placeholder = "* Имя"]']  # поле ввода Имя
    input_lastname = [By.XPATH, './/input[@placeholder = "* Фамилия"]']  # поле ввода Фамилия
    input_address = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]']  # поле ввода Адрес
    input_station = [By.XPATH, './/input[@placeholder = "* Станция метро"]']  # поле ввода Станция метро
    input_number = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]']  # поле ввода Номер телефона
    input_date = [By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]']  # поле ввода даты получения самоката
    input_comment = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]']  # поле ввода комментария для курьера
    renta = [By.XPATH, './/div[text() = "* Срок аренды"]']  #  пол ввода срока аренды

    button_next = [By.XPATH, './/button[text() = "Далее"]']  # кнопка "Далее"
    button_order = [By.XPATH, './/div[@class = "Order_Buttons__1xGrp"]//button[text() = "Заказать"]']  # кнопка подтверждения заказа "Заказать"
    button_yes = [By.XPATH, './/button[text() = "Да"]']  # кнопка подтверждения "Да"
    button_station = [By.CLASS_NAME, 'select-search__select']  # поле станций метро

    period_1 = [By.XPATH, './/div[text() = "двое суток"]']  # выбор срока аренды на 2 суток
    period_2 = [By.XPATH, './/div[text() = "пятеро суток"]']  # выбор срока аренды на 5 суток

    chb_black = [By.XPATH, './/label[@for = "black"]']  # цвет самоката "Черный жемчуг"
    chb_grey = [By.XPATH, './/label[@for = "grey"]']  # цвет самоката "Серая безысходность"

    success_order = [By.XPATH, './/button[text() = "Посмотреть статус"]']  # кнопка "Посмотреть статус" в уведомлении успешного заказа
    emty_place = [By.CLASS_NAME, 'App_App__15LM-']  # пусто место для клика
