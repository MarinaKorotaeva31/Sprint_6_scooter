from selenium.webdriver.common.by import By

class LocatorsBasePage:
    logo_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']  # лого "Самокат"
    logo_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']  # локо "Яндекс"
    yandex = [By.CLASS_NAME, 'dzen-layout--header-micro-app__header-1m']  # локатор на странице Дзена